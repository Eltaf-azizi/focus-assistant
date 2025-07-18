<h1 align="center">🚀 Focus Assistant</h1>

An AI-powered personal productivity assistant that helps you stay organized, focused, and efficient — built with Flask, ChromaDB, and professional-grade deployment tools.


## 💡 What You'll Learn

- ✅ How to set up and structure a Python project using **Flask**
- 🧠 Integrate **AI capabilities** to create a smart assistant
- 📚 Store and retrieve context-rich data using **ChromaDB**
- ☁️ Deploy your app to the cloud using **CI/CD pipelines**
- 🐳 Use **Docker**, **GitHub Actions**, and **AWS** for scalable, maintainable deployment



## 📌 Why Focus Assistant?

- Perfect for **beginners** looking to learn full-stack Python development  
- Build a **real-world AI application** from scratch  
- Learn hands-on skills in development, deployment, and cloud integration  
- Gain experience working with **vector databases**, APIs, and automation tools



## 🛠️ Tech Stack

| Tool/Tech         | Purpose                         |
|-------------------|----------------------------------|
| **Python**        | Core programming language        |
| **Flask**         | Web framework                    |
| **ChromaDB**      | Vector database for embeddings   |
| **LangChain**     | AI orchestration (if applicable) |
| **Docker**        | Containerization                 |
| **GitHub Actions**| CI/CD automation                 |
| **AWS**           | Cloud deployment (EC2/S3/etc.)   |



## 📁 Project Structure 

    focus-assistant/
    ├── .github/
    │   └── workflows/
    │       └── .gitkeep
    ├── backend/
    │   ├── ingest_data.py         # Handles data ingestion into ChromaDB
    │   └── model.py               # AI logic or LLM integration
    ├── static/
    │   ├── app.js                 # Frontend JS logic
    │   └── style.css              # Styling for the web interface
    ├── templates/
    │   └── index.html             # Main UI page (Jinja2 template)
    ├── .env                       # Environment variables
    ├── app.py                     # Main Flask app
    ├── template.py                # (Likely) rendering logic or additional template functions
    ├── Dockerfile                 # Docker container setup
    ├── requirements.txt           # Python dependencies
    ├── README.md                  # Project documentation


## 🚧 Features (Planned or Implemented)

- [x] User-friendly interface for daily planning  
- [x] AI assistant to answer personal productivity queries  
- [x] Store tasks, notes, and conversations in a vector DB  
- [ ] Natural language command execution  
- [ ] Daily summary and reminders  
- [ ] Slack or MS Teams integration (optional)


## 🧪 Getting Started

### 🔧 Prerequisites
- Python 3.10+
- Docker
- Git
- AWS CLI (optional)

### 🐍 Create your virtual environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Run the app
```bash
Copy
Edit
python main.py

```

## ☁️ Deployment
This project supports automatic deployment using:

 - GitHub Actions for CI/CD

 - Docker for containerized builds

 - AWS EC2 or Render for hosting

 - Steps are detailed in the /deploy folder (to be added).

## 🧠 Inspiration

Focus Assistant is part of a bigger vision to combine AI, productivity tools, and automation into everyday workflows for students, developers, and entrepreneurs.

## 🤝 Contributing
We welcome medical professionals & AI researchers to improve diagnostic accuracy!

 - Report issues for misdiagnoses

 - Suggest PubMed query optimizations

 - Add new symptom parsing rules

<h3 align="center">Happy Coding!</h3>

