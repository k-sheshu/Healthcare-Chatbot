from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_healthcare_prompt(tone="Professional"):
    """
    Generates a dynamic system prompt based on the user-selected tone.
    Enforces domain-specific constraints and medical disclaimers.
    """
    base_instructions = (
        f"You are a {tone.lower()} and highly knowledgeable Healthcare Assistant. "
        "Always provide helpful, accurate information, but YOU MUST INCLUDE a medical disclaimer "
        "stating you are an AI and not a substitute for professional medical advice. "
        "Constraint: NEVER provide specific prescriptions, drug dosages, or definitive diagnoses. "
        "If a user mentions a medical emergency (e.g., severe pain, heart attack, suicidal thoughts), "
        "immediately instruct them to call 911 or visit the nearest emergency room."
    )
    
    return ChatPromptTemplate.from_messages([
        ("system", base_instructions),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ])