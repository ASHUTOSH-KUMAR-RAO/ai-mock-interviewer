
# 🤖 AI Mock Interviewer

<div align="center">

![AI Mock Interviewer Banner](https://img.shields.io/badge/AI-Mock%20Interviewer-blue?style=for-the-badge&logo=robot)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-API-F55036?style=for-the-badge)](https://groq.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

**An AI-powered Mock Interviewer that remembers your entire conversation, asks role-based follow-up questions, and gives real-time feedback — built with LangChain + Groq + Streamlit.**

[🚀 Getting Started](#-getting-started) • [✨ Features](#-features) • [🛠️ Tech Stack](#-tech-stack) • [📸 Demo](#-demo) • [🤝 Contributing](#-contributing)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Demo](#-demo)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🧠 About the Project

**AI Mock Interviewer** is an intelligent conversational chatbot that simulates a real job interview experience. Unlike traditional quiz apps, this interviewer:

- **Remembers everything you said** — full conversation history using LangChain Memory
- **Asks smart follow-up questions** — based on your previous answers
- **Gives real-time feedback** — tells you exactly how to improve
- **Adapts to your role** — GenAI Engineer, ML Engineer, Python Developer, and more

> 💡 *Built as part of the GenAI + LangChain learning journey — Section 27: Building Chatbots With Conversation History Using LangChain*

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🧠 **Conversation Memory** | Remembers full interview history using LangChain `ConversationBufferMemory` |
| 🎯 **Role-Based Interviews** | Choose your role — GenAI, ML, Python, Data Science |
| 📝 **Real-Time Feedback** | AI evaluates your answer and tells you how to improve |
| 🔁 **Follow-Up Questions** | Asks intelligent follow-ups based on your previous answers |
| ⚡ **Groq Powered** | Super fast LLM responses using Groq API |
| 🎨 **Clean UI** | Minimal and intuitive Streamlit interface |
| 🔒 **Secure** | API keys stored safely in `.env` file |
| 📊 **Interview Summary** | Get a full performance summary at the end |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🦜 **LangChain** | Chains, Memory, Prompt Templates |
| ⚡ **Groq API** | Fast LLM inference (LLaMA 3) |
| 🎨 **Streamlit** | Frontend UI |
| 🐍 **Python 3.11** | Core language |
| 🔑 **python-dotenv** | Environment variable management |
| 🧱 **LCEL** | LangChain Expression Language for chaining |

---

## 📁 Project Structure

```
ai-mock-interviewer/
│
├── src/                        # Core source code
│   ├── __init__.py
│   ├── chains.py               # LangChain LCEL chains
│   ├── memory.py               # Conversation memory setup
│   └── prompts.py              # Prompt templates
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .env                        # Your actual API keys (git ignored)
├── .gitignore                  # Files to ignore in git
├── CHANGELOG.md                # Version history
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
└── README.md                   # You are here!
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.11+
- Conda (recommended)
- Groq API Key — [Get it here](https://console.groq.com)
- Git

---

### 📦 Installation

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-mock-interviewer.git
cd ai-mock-interviewer
```

#### 2. Create and activate conda environment

```bash
conda create -n mock-interviewer python=3.11 -y
conda activate mock-interviewer
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Setup environment variables

```bash
cp .env.example .env
```

Now open `.env` and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
```

#### 5. Run the app

```bash
streamlit run app.py
```

🎉 Open your browser at `http://localhost:8501`

---

## 🎮 Usage

1. **Select your interview role** from the sidebar (GenAI / ML / Python)
2. **Start the interview** — AI will ask you the first question
3. **Type your answer** in the chat box
4. **Get instant feedback** + follow-up question
5. **End the interview** to get your full performance summary

---

## 📸 Demo

> 🔥 Coming Soon — Screenshot & Live Demo link will be added here!

---

## 🗺️ Roadmap

- [x] Basic chatbot with conversation memory
- [x] LangChain + Groq integration
- [x] Streamlit UI
- [ ] Role-based interview modes
- [ ] Performance scoring system
- [ ] Interview summary report (PDF export)
- [ ] Resume upload & personalized questions
- [ ] Voice input support
- [ ] Deploy on Streamlit Cloud

---

## 🤝 Contributing

Contributions are welcome and appreciated! 🙌

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

```bash
# Quick contribution setup
git clone https://github.com/ASHUTOSH-KUMAR-RAO/ai-mock-interviewer.git
git checkout -b feature/your-feature-name
# make changes
git commit -m "feat: your feature"
git push origin feature/your-feature-name
# open Pull Request
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ashutosh Kumar Rao**

[![GitHub](https://img.shields.io/badge/GitHub-your-username-181717?style=for-the-badge&logo=github)]([https://github.com/your-username](https://github.com/ASHUTOSH-KUMAR-RAO))
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-username)

---

<div align="center">

Made with ❤️ by **Ashutosh Kumar Rao**

⭐ **Star this repo if you found it helpful!** ⭐

</div>
