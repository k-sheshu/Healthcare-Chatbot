import os
import logging
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompts import get_healthcare_prompt

# Setup Built-in Python Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

def get_chatbot_response(user_input, chat_history, tone="Professional"):
    try:
        logging.info(f"Received user query. Selected Tone: {tone}")
        
        # 1. Token Usage Optimization: Keep only the last 5 conversation turns (10 messages)
        MAX_MESSAGES = 10
        if len(chat_history) > MAX_MESSAGES:
            optimized_history = chat_history[-MAX_MESSAGES:]
            logging.info("Trimmed chat history to optimize tokens.")
        else:
            optimized_history = chat_history
        
        # 2. Initialize Model (Using low temperature for factual healthcare responses)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
        
        # 3. Fetch Configurable Prompt
        prompt_template = get_healthcare_prompt(tone)
        
        # 4. Execute Chain
        chain = prompt_template | llm
        response = chain.invoke({
            "input": user_input,
            "chat_history": optimized_history
        })
        
        logging.info("Successfully generated response from Gemini API.")
        return response.content

    except Exception as e:
        # Proper exception handling and fallback mechanism
        logging.error(f"API Error occurred: {str(e)}")
        return "⚠️ I'm currently experiencing technical difficulties connecting to the healthcare database. Please try again in a moment."