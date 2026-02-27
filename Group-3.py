"""
===========================================================
                    AutoDebug AI
              Autonomous API Debugging Agent
===========================================================

Group Number: 3  

Project Overview:
AutoDebug AI is an intelligent API debugging assistant powered
by LLM-based reasoning. It automatically tests API endpoints,
detects errors, analyzes failure causes, and generates structured
corrective solutions.

Problem Statement:
Manual API debugging is repetitive and time-consuming.
Developers often struggle with unclear error messages and
misconfigured endpoints. This project automates that process.

Core Workflow:
1. Accept API endpoint and HTTP method from user.
2. Execute request using Python requests library.
3. Detect HTTP errors (404, 401, 500, etc.).
4. Send structured error details to OpenAI API.
5. Generate:
   - Root cause analysis
   - Suggested fix
   - Corrected code snippet
6. Display results using Gradio UI.

Technology Stack:
- Python
- Gradio
- OpenAI API
- Requests
- Git & GitHub

GitHub Repository:
https://github.com/anam-09/auto-debug-ai

Key Features:
- Automatic API testing
- AI-powered root cause analysis
- Suggested fixes
- Corrected code generation
- Execution logs viewer
- Clean Gradio UI

===========================================================
"""

def main():
    print("======================================")
    print("  AutoDebug AI - Project Submission  ")
    print("======================================")
    print("Group Number: 3")  
    print("\nGitHub Repository:")
    print("https://github.com/anam-09/auto-debug-ai")
    print("\nStatus: Ready for Evaluation ")

if __name__ == "__main__":
    main()