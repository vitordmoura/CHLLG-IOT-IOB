# Reconhecimento Facial + Emoções

Este projeto utiliza **OpenCV** e **DeepFace** para detectar **rostos, olhos e boca** em tempo real pela webcam, além de identificar **emoções** (Feliz, Triste e Bravo).

---

## 🎯 Objetivo
Demonstrar como técnicas de visão computacional podem ser aplicadas para reconhecimento facial e análise de emoções em tempo real, com ajustes dinâmicos de parâmetros.  
Este projeto é parte da **Challenge**, integrando tecnologia ao contextto do atendimento psicológico.

---

## ▶️ Execução
Para rodar o projeto:

```bash
git clone https://github.com/vitordmoura/CHLLG-IOT-IOB.git
cd CHLLG-IOT-IOB
pip install -r requirements.txt
python main.py

```

## 📦 Dependências
As principais bibliotecas utilizadas são:

- **opencv-python** → captura e processamento de imagens  
- **deepface** → análise de emoções  
- **tensorflow, keras, numpy, pandas** → dependências do DeepFace  

---

## ⚙️ Parâmetros ajustáveis
Durante a execução, você pode ajustar:

- `+` / `-` → altera **scaleFactor** (sensibilidade da detecção)  
- `]` / `[` → altera **minNeighbors** (precisão da detecção)  
- `s` → encerra o programa  

Esses parâmetros influenciam diretamente a estabilidade e a confiabilidade da detecção:

- **scaleFactor**: valores menores tornam a detecção mais sensível, mas instável; valores maiores deixam mais firme, mas podem perder rostos pequenos.  
- **minNeighbors**: valores baixos detectam mais rostos, mas com falsos positivos; valores altos reduzem erros, mas podem ignorar rostos reais.  
- **minSize**: define o tamanho mínimo do rosto detectado.  

---

## 📌 Observações
- O modelo **DeepFace** pode demorar alguns segundos para carregar na primeira execução.  
- Iluminação uniforme ajuda a reduzir oscilações na detecção.  
- Os arquivos Haar Cascade (`haarcascade_frontalface_default.xml`, `haarcascade_eye.xml`, `haarcascade_smile.xml`) devem estar disponíveis na pasta do projeto.  

---

## ⚖️ Nota Ética sobre uso de dados faciais
Este projeto é **educacional** e não deve ser usado em aplicações que envolvam coleta, armazenamento ou compartilhamento de dados faciais sem consentimento.  
Reconhecimento facial e análise de emoções envolvem informações pessoais sensíveis. O uso em ambientes reais deve respeitar:

- **Privacidade** dos indivíduos  
- **Consentimento explícito** antes da captura  
- **Finalidade clara e transparente**  
- **Conformidade legal** com a LGPD (Lei Geral de Proteção de Dados) e outras legislações aplicáveis  

O objetivo aqui é **demonstrar técnicas de visão computacional**, não criar sistemas de vigilância ou monitoramento.
