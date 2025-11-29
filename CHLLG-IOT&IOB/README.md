# Reconhecimento Facial + Emoções

Este projeto usa **OpenCV** e **DeepFace** para detectar **rostos, olhos e boca** pela webcam e mostrar **emoções** (Feliz, Triste e Bravo).

## 🚀 Funcionalidades
- Detecção de rosto, olhos e boca com Haar Cascade
- Reconhecimento de emoções com DeepFace
- Cores diferentes para cada emoção:
  - Feliz → Amarelo
  - Triste → Azul
  - Bravo → Vermelho
- Ajuste em tempo real:
  - `+` / `-` → sensibilidade (`scaleFactor`)
  - `]` / `[` → precisão (`minNeighbors`)
  - `s` → sair

## ⚙️ Requisitos
   - Python 3.8 ou superior
   - Webcam funcional
   - Sistema operacional: Windows, Linux ou macOS
    - Bibliotecas listadas em requirements.txt
 

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/vitordmoura/CHLLG-IOT-IOB.git
cd CHLLG-IOT-IOB
pip install -r requirements.txt




