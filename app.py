import streamlit as st
from src.chatbot_engine import get_chatbot_response
from langchain_core.messages import HumanMessage, AIMessage

# 1. Configuration-Driven UI setup
st.set_page_config(page_title="Healthcare AI", page_icon="🏥", layout="wide")

with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Configure the assistant's behavior:")
    selected_tone = st.selectbox(
        "Assistant Tone", 
        ["Professional", "Empathetic", "Direct & Clinical"]
    )
    st.info("Disclaimer: This bot is for informational purposes only. Do not use for emergencies.")
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

st.title("🏥 Healthcare AI Support")
st.caption("Advanced Domain-Specific Chatbot with Native Logging & Token Optimization")

# 2. Session-based memory management
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Conversation History
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# 3. Chat Input & Processing
if prompt := st.chat_input("Describe your symptoms or ask a health question..."):
    
    # Save and display user input
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Consulting medical guidelines..."):
            # Pass history (excluding the user message we just appended)
            history_for_api = st.session_state.messages[:-1]
            
            response_text = get_chatbot_response(
                user_input=prompt, 
                chat_history=history_for_api,
                tone=selected_tone
            )
            st.markdown(response_text)
    
    # Save AI response to memory
    st.session_state.messages.append(AIMessage(content=response_text))