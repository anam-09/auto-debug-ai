AutoDebug AI
Autonomous API Debugging Agent powered by LLM Reasoning
🧠 Problem

Debugging failing APIs is time-consuming.

Developers often:

Manually inspect logs

Reproduce errors

Guess root causes

Rewrite incorrect requests

This slows down development and deployment.

💡 Solution

AutoDebug AI is an autonomous debugging agent that:

Sends API requests (GET / POST)

Detects failures (404, 401, 500, etc.)

Uses LLM reasoning to analyze the error

Suggests fixes

Generates corrected Python code

It transforms debugging from reactive → autonomous.

🏗 How It Works
User Input (Endpoint + Method)
        ↓
API Request Execution
        ↓
Error Detection
        ↓
LLM Error Analysis
        ↓
Structured JSON Response
        ↓
Fix Suggestion + Corrected Code
⚙️ Tech Stack

Python

Gradio (UI)

Requests

OpenAI API

GitHub Push Protection (Security best practices)

🖥 Features

🔍 Automatic API testing

🤖 AI-powered root cause analysis

🛠 Suggested fixes

💻 Corrected code generation

📜 Execution logs viewer

🎨 Clean Gradio UI

🚀 Installation
1️⃣ Clone Repository
git clone https://github.com/anam-09/auto-debug-ai.git
cd auto-debug-ai
2️⃣ Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add OpenAI API Key

Create a .env file:

OPENAI_API_KEY=your_api_key_here

⚠️ Do NOT push this file to GitHub.

▶️ Run the Application
python app.py

Open the Gradio link in your browser.

🧪 Example Test Endpoints

Working:

https://jsonplaceholder.typicode.com/posts/1

Failing:

https://jsonplaceholder.typicode.com/post
📂 Project Structure
auto-debug-ai/
│
├── agents/
│   ├── analyzer.py
│   ├── tools.py
│   ├── api_analyzer.py
│   └── backend_api.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
🔐 Security

Uses environment variables for API keys

GitHub Push Protection enabled

.env excluded from repository

🔮 Future Improvements

CI/CD integration

Retry automation

Multi-step reasoning

Deployment monitoring integration

Slack/Discord alerts

Docker support

