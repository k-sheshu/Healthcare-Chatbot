# 🏥 Production-Ready Healthcare GenAI Chatbot

## 1. Project Overview
A domain-specific, production-ready chatbot designed to provide healthcare guidance. Powered by the Google Gemini API, it features strict role-based constraints, multi-turn conversation memory, and a clean, modular architecture.

## 2. System Architecture
User -> Streamlit UI -> Backend Engine (LangChain) -> Prompt Management -> Gemini API -> UI Rendering

## 3. Features
* **Modular Codebase:** Complete separation of UI, API handling, and prompt management.
* **Contextual Memory:** Maintains structured chat history using session state.
* **Robust Error Handling:** Built-in fallback mechanisms for API failures.
* **Token Optimization:** Rolling memory window to prevent context overflow.

## 4. Local Setup Instructions
1. Clone the repository: `git clone <your-repo-link>`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: 
   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your Google API key: `GOOGLE_API_KEY=your_key`
6. Run the application: `streamlit run app.py`

## 5. AWS EC2 Deployment Steps
1. Launch an Ubuntu EC2 instance and expose port `8501` in the Security Group.
2. Connect via SSH and clone the GitHub repository.
3. Install Python, pip, and venv: `sudo apt install python3-pip python3-venv`
4. Set up the virtual environment and install requirements.
5. Create the `.env` file directly on the server for security.
6. Run the app in the background using `tmux`:
   * `tmux new -s chatbot`
   * `streamlit run app.py`
   * Detach session (`Ctrl+B`, then `D`).
