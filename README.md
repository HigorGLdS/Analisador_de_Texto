# 📊 Analisador de Texto

Este projeto é um **analisador de texto em Python**, capaz de processar arquivos `.txt`, remover pontuações, normalizar o conteúdo e gerar estatísticas de frequência das palavras utilizadas.  
É uma ferramenta útil para estudos de **linguística**, **análise de dados textuais** ou mesmo para treinar técnicas de **processamento de linguagem natural (NLP)**.

---

## 🚀 Funcionalidades
- ✅ Leitura de arquivos de texto (`.txt`)  
- ✅ Limpeza de texto (remoção de pontuações e padronização para minúsculas)  
- ✅ Tokenização em palavras usando **NLTK**  
- ✅ Contagem de frequência das palavras  
- ✅ Geração de relatório salvo em `.txt` na pasta `resultados`  

---

## 📂 Estrutura do Projeto

M1_S4_AnalisadorTexto/
├── README.md
├── requirements.txt
├── analisador.py
├── textos/
│ └── exemplo.txt
└── resultados/
└── frequencias.txt

---

## 🛠️ Tecnologias Utilizadas
- [Python 3](https://www.python.org/)  
- [NLTK](https://www.nltk.org/) (Natural Language Toolkit)  

---

## 📦 Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/M1_S4_AnalisadorTexto.git
cd M1_S4_AnalisadorTexto

pip install -r requirements.txt

python analisador.py