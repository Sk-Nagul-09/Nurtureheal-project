# Nurtureheal-project-3

# CI/CD Pipeline for Flask Application using GitHub Actions and Docker

## 📘 Project Overview
This project demonstrates a complete **CI/CD pipeline** for a simple **Python Flask web application**.  
The goal is to automate the build, test, and deployment process using **GitHub Actions**, **Docker**, and **AWS**, while integrating **monitoring** and **security scanning** tools.

---

## 🚀 Objective
To set up a mini CI/CD pipeline that:
- Builds and containerizes a Flask application using Docker.
- Deploys the app automatically to AWS EC2 via GitHub Actions.
- Implements monitoring using AWS CloudWatch.
- Performs vulnerability scanning using Trivy.
- Demonstrates cost-awareness and security best practices.

---

## 🧩 Tools and Technologies
| Category | Tools Used |
|-----------|-------------|
| Operating System | Linux (Amazon Linux) |
| Cloud Platform | AWS EC2 |
| CI/CD Tool | GitHub Actions |
| Containerization | Docker |
| Monitoring | AWS CloudWatch |
| Security Scan | Trivy |
| Version Control | Git, GitHub |
| Programming | Python (Flask) |

---

## ⚙️ Pipeline Workflow
1. **Code pushed to GitHub** triggers the GitHub Actions workflow.
2. **Build Stage:** Docker builds the image for the Flask app.
3. **Test Stage:** The pipeline runs basic tests (curl to check response).
4. **Deploy Stage:** The container is deployed to the AWS EC2 instance.
5. **Monitoring:** AWS CloudWatch tracks instance metrics (CPU, memory, uptime).
6. **Security Scan:** Trivy scans the Docker image for vulnerabilities.

---

## 🐳 Docker Setup
Build and run locally:
```bash
docker build -t drviki-app .
docker run -p 8080:8080 drviki-app
Access the app at:
http://localhost:8080

🔐 Security and Cost Optimization
Security: Docker image scanned with Trivy to detect known vulnerabilities.

Cost Optimization: Implemented measures like stopping idle EC2 instances and using autoscaling for dynamic load management.

📊 Monitoring
Used AWS CloudWatch to visualize:

Instance uptime

CPU and memory utilization

Application request metrics

🖼️ Visual Outputs
✅ GitHub Actions pipeline screenshot (build → test → deploy)

✅ Docker container running

✅ AWS CloudWatch metrics view

✅ Trivy vulnerability scan summary

📁 Repository Structure
bash
Copy code
.
├── app.py                # Flask application source
├── Dockerfile            # Docker image setup
├── requirements.txt      # Python dependencies
├── .github/workflows/    # GitHub Actions workflow file
│   └── deploy.yml
└── README.md             # Project documentation

🧠 Key Learnings
Automated CI/CD using GitHub Actions.

Containerized apps for consistent deployments using Docker.

Integrated monitoring and security checks in deployment workflow.

Gained awareness of cloud cost management strategies.

👤 Author
Sk Nagul
📧 Email: Sknagul.awsdevops@gmail.com
