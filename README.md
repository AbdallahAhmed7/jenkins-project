# 🌌 Cyber Clock – Jenkins CI/CD Pipeline

A cyberpunk-themed live clock web app deployed automatically using a Jenkins CI/CD pipeline with Docker.

---

## 📋 Project Overview

This project demonstrates a complete CI/CD pipeline built with Jenkins that automatically:
1. **Builds** a Docker image from the source code
2. **Tests** the application using pytest
3. **Deploys** the app as a running Docker container

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python + Flask | Web application |
| Docker Desktop | Container runtime |
| Jenkins | CI/CD automation server |
| pytest | Automated testing |

## 📁 Project Structure
```
jenkins-project/
├── app.py            # Flask web application
├── test_app.py       # Automated tests
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker image definition
└── Jenkinsfile       # CI/CD pipeline definition
```

## ⚙️ Pipeline Stages
| Stage | What it does |
|-------|-------------|
| 🔨 Build | Builds a Docker image from the source code |
| 🧪 Test | Runs automated tests with pytest inside the container |
| 🚀 Deploy | Runs the app as a Docker container on port 8081 |

## 🌐 Access
| Service | URL |
|---------|-----|
| Jenkins Dashboard | http://localhost:8080 |
| Cyber Clock App | http://localhost:8081 |

---

## 👤 Author
**Abdallah Ahmed**

[![GitHub](https://img.shields.io/badge/GitHub-AbdallahAhmed7-181717?style=flat&logo=github)](https://github.com/AbdallahAhmed7)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-abdallahahmed7-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdallahahmed7/)
