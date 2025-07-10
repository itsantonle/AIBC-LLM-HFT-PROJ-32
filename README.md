# 🧠 AI Toolkit Demo (Tkinter + Transformers)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Transformers](https://img.shields.io/badge/HuggingFace-FFBF00?style=for-the-badge&logo=huggingface&logoColor=black)
![Tkinter](https://img.shields.io/badge/Tkinter-Basic%20GUI-blue?style=for-the-badge)
![NLTK](https://img.shields.io/badge/NLTK-Natural%20Language%20Toolkit-green?style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)

---

## ⚠️ Note

![Python Version](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)

_This project requires Python 3.9 or higher. It uses Hugging Face Transformers and NLTK for NLP tasks, PyTorch for model inference, and Tkinter for GUI._

---

## 🧰 Features

- 🧠 **Named Entity Recognition (NER)**  
  Uses `dslim/bert-base-NER` to extract and explain entities like people, locations, and organizations.

- 💬 **Sentiment + POS Analyzer**  
  Combines `distilbert-base-uncased-finetuned-sst-2-english` with NLTK to detect sentiment and extract the most frequent verb and adjective.

- 🧠 **Zero-Shot Classifier**  
  Uses `facebook/bart-large-mnli` to classify any sentence into user-defined categories — no retraining needed.

- 🖥️ **Tkinter GUI Launcher**  
  A main window lets you launch each tool independently with a clean interface and feedback label.

---

## 🚀 Installation
_Recommended a good CPU and ample space for the models_
### 1. **Clone the repository**
```bash
git clone https://github.com/itsantonle/AIBC-LLM-HFT-PROJ-32.git
```
### 2. **Install dependencies**
```bash
pip install -r requirements.txt
```
### 3. **Make sure Pytorch is installed**
```bash
pip install torch
```

## 🧠Usage 
_Broken up into parts_

### **HFT**
  - navigate to hft folder
``bash
cd hft
``
  - run the main gui
``bash
python main.py
``

