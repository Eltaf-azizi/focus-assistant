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

    .
    ├── .github/workflows/ # CI/CD pipeline setup
    │ └── cicd.yaml
    ├── backend/ # Backend logic and data ingestion
    │ ├── ingest_data.py
    │ └── model.py
    ├── Data/ # Sample data (e.g., PDFs)
    │ └── Medical_book.pdf
    ├── src/ # Core logic
    │ ├── init.py
    │ ├── helper.py
    │ └── prompt.py
    ├── static/ # Static files (CSS)
    │ └── styles.css
    ├── templates/ # HTML templates
    │ └── index.html
    ├── .env # Environment variables
    ├── .dockerignore
    ├── .gitignore
    ├── app.py # Flask application
    ├── Dockerfile # Docker container setup
    ├── README.md # Project documentation
    ├── requirements.txt # Python dependencies
    ├── setup.py # Setup script for packaging
    ├── store_index.py # Vector store handler
    └── template.py # Base template file


## 🚀 Features

- 🔍 **AI Assistance** using prompt engineering
- 📄 **PDF Document Parsing** (e.g., Medical_book.pdf)
- 🧠 **Contextual Answering** using embeddings
- 🌐 **Web Interface** using Flask (HTML + CSS)
- 📦 **Dockerized** for easy deployment
- 🔁 **CI/CD Pipeline** via GitHub Actions


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

