import cv2
from deepface import DeepFace

# Caminhos dos classificadores Haar
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

# Verificação de carregamento
if face_cascade.empty() or eye_cascade.empty() or smile_cascade.empty():
    print("Erro ao carregar um dos arquivos Haar Cascade. Verifique os caminhos.")
    exit(1)

# Abre a webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
    exit(1)

# Parâmetros ajustáveis
scale_factor = 1.2
min_neighbors = 6
min_size = (100, 100)

# Mapeamento de cores por emoção (apenas 3)
emotion_colors = {
    "happy": (0, 255, 255),   # amarelo
    "sad": (255, 0, 0),       # azul
    "angry": (0, 0, 255)      # vermelho
}

# Tradução das emoções para português
emotion_translation = {
    "happy": "Feliz",
    "sad": "Triste",
    "angry": "Bravo"
}

print("Pressione 's' para sair. Use '+'/'-' para scaleFactor, ']'/'[' para minNeighbors.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame não capturado.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detector rosto
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size
    )

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detector olhos (branco)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 255), 2)

        # Detector boca (azul)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)

        # Reconhecimento de emoção com DeepFace
        try:
            result = DeepFace.analyze(frame[y:y+h, x:x+w], actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion'].lower()

            # Só aceita Feliz, Triste ou Bravo
            if emotion in emotion_translation:
                emotion_pt = emotion_translation[emotion]
                color = emotion_colors[emotion]
            else:
                emotion_pt = "Desconhecido"
                color = (0, 255, 0)  # padrão verde

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"Sentimento: {emotion_pt}", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        except Exception:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Sentimento: N/A", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    # HUD com parâmetros
    hud = f"Faces: {len(faces)} | scaleFactor: {scale_factor:.2f} | minNeighbors: {min_neighbors}"
    cv2.putText(frame, hud, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Reconhecimento Facial + Sentimentos", frame)

    # Controle de teclas
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        break
    elif key == ord('+'):
        scale_factor = max(1.01, scale_factor - 0.01)
    elif key == ord('-'):
        scale_factor = scale_factor + 0.01
    elif key == ord(']'):
        min_neighbors = min_neighbors + 1
    elif key == ord('[') and min_neighbors > 1:
        min_neighbors = min_neighbors - 1

cap.release()
cv2.destroyAllWindows()
