# 🤖 Auto Debug AI

Auto Debug AI is an intelligent debugging assistant designed to help developers quickly identify, understand, and resolve errors in code.  
The project focuses on improving debugging efficiency and learning by providing clear explanations and suggestions for common issues.

This repository follows proper **GitHub collaboration, branching, and version control practices**, making it suitable for academic, internship, and team-based development.

---

## 📌 Project Description

Debugging is often time-consuming and confusing, especially for beginners.  
**Auto Debug AI** aims to simplify this process by:
- Analyzing errors
- Explaining the root cause
- Suggesting possible fixes
- Supporting collaborative development

The project is fully implemented and maintained using Git best practices.

---

## 🎯 Key Features

- Intelligent error analysis
- Clear and beginner-friendly explanations
- Modular and clean code structure
- Team collaboration using Git branches
- Python virtual environment support
- Ready for academic and professional use

---

## 🛠️ Technology Stack

- **Programming Language:** Python  
- **Version Control:** Git  
- **Repository Hosting:** GitHub  
- **Environment Management:** Python Virtual Environment (`myenv`)  

---

## 📁 Project Structure
auto-debug-ai/
│── src/ # Core source code
│── utils/ # Utility/helper functions
│── tests/ # Test cases
│── myenv/ # Virtual environment (ignored in Git)
│── README.md # Project documentation
│── requirements.txt # Project dependencies


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anam-09/auto-debug-ai.git
cd auto-debug-ai
python -m venv myenv
.\myenv\Scripts\Activate.ps1
pip install -r requirements.txt

Team Collaboration Workflow

Each contributor works on a separate branch

Direct pushes to main are avoided

All changes are merged using Pull Requests

Branch Naming Convention

feature-new-module

bugfix-error-handler

docs-update

Git Workflow Used
git checkout main
git pull
git checkout -b feature-name
git add .
git commit -m "Meaningful commit message"
git push origin feature-name

