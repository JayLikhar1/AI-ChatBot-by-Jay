# An AI-Powered ChatBot App — 100% free to use

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# --- Minimal Apple/iOS Design ---
APPLE_CSS = """
<style>
/* Apple System Font Stack */
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "SF Pro", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    font-weight: 400 !important;
    letter-spacing: -0.01em !important;
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
}

/* Apple Dark Mode Colors */
html, body {
    background-color: #000000 !important;
    color: #ffffff !important;
}

.stApp {
    background-color: #000000 !important;
}

/* Main content container */
.main .block-container {
    padding: 3rem 2rem 8rem !important;
    max-width: 680px !important;
    margin: 0 auto !important;
    background-color: transparent !important;
}

/* Header */
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0.8) !important;
    backdrop-filter: blur(20px) saturate(180%) !important;
    border-bottom: 0.5px solid rgba(255, 255, 255, 0.1) !important;
}

footer {
    visibility: hidden !important;
}

/* Typography - Apple Style */
h1 {
    font-size: 2rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.03em !important;
    color: #ffffff !important;
    margin-top: 0 !important;
    margin-bottom: 0.5rem !important;
    line-height: 1.1 !important;
}

h2, .stMarkdown h2 {
    font-size: 1rem !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    color: rgba(255, 255, 255, 0.8) !important;
}

p, .stMarkdown p, .stMarkdown {
    font-size: 1rem !important;
    line-height: 1.5 !important;
    color: rgba(255, 255, 255, 0.9) !important;
    font-weight: 400 !important;
}

.stCaption {
    font-size: 0.875rem !important;
    color: rgba(255, 255, 255, 0.6) !important;
    font-weight: 400 !important;
    letter-spacing: -0.01em !important;
}

/* Sidebar - Apple Style */
[data-testid="stSidebar"] > div:first-child {
    background-color: #1d1d1f !important;
    border-right: 0.5px solid rgba(255, 255, 255, 0.1) !important;
}

[data-testid="stSidebar"] .stMarkdown {
    color: rgba(255, 255, 255, 0.9) !important;
}

[data-testid="stSidebar"] h1 {
    font-size: 1.25rem !important;
    font-weight: 600 !important;
    color: #ffffff !important;
    letter-spacing: -0.02em !important;
}

[data-testid="stSidebar"] h2 {
    font-size: 0.8125rem !important;
    font-weight: 600 !important;
    color: rgba(255, 255, 255, 0.6) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] .stMarkdown p {
    color: rgba(255, 255, 255, 0.8) !important;
}

/* Chat Messages - Minimal Apple Style */
[data-testid="stChatMessage"] {
    background-color: #1d1d1f !important;
    border-radius: 18px !important;
    padding: 1rem 1.25rem !important;
    margin-bottom: 1rem !important;
    border: 0.5px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
}

[data-testid="stChatMessage"] .stMarkdown {
    color: rgba(255, 255, 255, 0.9) !important;
    line-height: 1.5 !important;
    font-size: 1rem !important;
}

/* Chat Input - Apple Style */
[data-testid="stChatInput"] {
    border-radius: 20px !important;
    background-color: #1d1d1f !important;
    border: 0.5px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3) !important;
}

[data-testid="stChatInput"]:focus-within {
    border-color: rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4) !important;
}

[data-testid="stChatInput"] textarea {
    font-size: 1rem !important;
    padding: 1rem 1.25rem !important;
    background-color: transparent !important;
    color: #ffffff !important;
    border: none !important;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", sans-serif !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(255, 255, 255, 0.5) !important;
}

[data-testid="stChatInput"] button {
    border-radius: 18px !important;
    background-color: #007AFF !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 600 !important;
    transition: opacity 0.2s ease !important;
}

[data-testid="stChatInput"] button:hover {
    opacity: 0.9 !important;
}

[data-testid="stChatInput"] button:active {
    opacity: 0.8 !important;
}

/* Buttons - Apple Style */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.25rem !important;
    background-color: #1d1d1f !important;
    color: #007AFF !important;
    border: 0.5px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
    transition: opacity 0.2s ease, background-color 0.2s ease !important;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", sans-serif !important;
}

.stButton > button:hover {
    background-color: #2d2d2f !important;
    opacity: 1 !important;
}

.stButton > button:active {
    opacity: 0.7 !important;
}

/* Selectbox - Apple Style */
[data-testid="stSelectbox"] > div {
    border-radius: 10px !important;
    background-color: #1d1d1f !important;
    border: 0.5px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
}

[data-testid="stSelectbox"] select {
    background-color: transparent !important;
    color: #ffffff !important;
    border: none !important;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", sans-serif !important;
}

/* Dividers - Apple Style */
hr {
    border: none !important;
    border-top: 0.5px solid rgba(255, 255, 255, 0.1) !important;
    margin: 1.5rem 0 !important;
}

/* Alerts - Apple Style */
.stAlert {
    border-radius: 12px !important;
    background-color: #1d1d1f !important;
    border: 0.5px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
}

[data-baseweb="notification"] {
    background-color: #1d1d1f !important;
    color: rgba(255, 255, 255, 0.9) !important;
}

[data-testid="stSuccess"] {
    background-color: rgba(52, 199, 89, 0.1) !important;
    border-color: rgba(52, 199, 89, 0.3) !important;
    color: #34C759 !important;
}

[data-testid="stError"] {
    background-color: rgba(255, 59, 48, 0.1) !important;
    border-color: rgba(255, 59, 48, 0.3) !important;
    color: #FF3B30 !important;
}

[data-testid="stInfo"] {
    background-color: rgba(0, 122, 255, 0.1) !important;
    border-color: rgba(0, 122, 255, 0.3) !important;
    color: #007AFF !important;
}

[data-testid="stSpinner"] {
    color: #007AFF !important;
}

/* Scrollbar - Apple Style */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background-color: #000000;
}

::-webkit-scrollbar-thumb {
    background-color: rgba(255, 255, 255, 0.2);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background-color: rgba(255, 255, 255, 0.3);
}

/* Ensure visibility */
.stMarkdown, p {
    opacity: 1 !important;
    visibility: visible !important;
}

.main .block-container {
    opacity: 1 !important;
    visibility: visible !important;
}

[data-testid="stChatMessage"] {
    opacity: 1 !important;
    visibility: visible !important;
}
</style>
"""

# --- Provider: Groq ---
def get_llm(provider):
    """Return (llm, None) or (None, error_message)."""
    if provider == "groq":
        try:
            from langchain_groq import ChatGroq
        except ImportError:
            return None, "Install: `pip install langchain-groq`. Then set **GROQ_API_KEY** in `.env`. **Free key:** [console.groq.com](https://console.groq.com)"
        key = os.getenv("GROQ_API_KEY")
        if not key or not key.strip():
            return None, "Set **GROQ_API_KEY** in `.env`. **Free key:** [console.groq.com](https://console.groq.com)"
        return ChatGroq(model="llama-3.1-8b-instant", temperature=0.7, groq_api_key=key), None

    return None, "Unknown provider"


# Provider is always Groq
PROVIDERS = {"Groq": "groq"}  # Kept for compatibility, not used in UI - no need for PROVIDERS dict

st.set_page_config(
    page_title="AI ChatBot",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.markdown(APPLE_CSS, unsafe_allow_html=True)

st.title("AI-Powered Chatbot by Jay Likhar")
st.caption("Powered by Groq")
st.markdown("""
<div style='margin-top: 0.5rem; margin-bottom: 1.5rem; color: #b1bac4; line-height: 1.6;'>
    An intelligent chatbot powered by Groq's fast AI models. Ask questions, get instant responses, 
    and enjoy seamless conversations with advanced language understanding.
</div>
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "provider_key" not in st.session_state:
    st.session_state.provider_key = "groq"

# --- Sidebar: llm init ---
with st.sidebar:
    st.title("Settings")
    labels = list(PROVIDERS.keys())
    idx = list(PROVIDERS.values()).index(st.session_state.provider_key) if st.session_state.provider_key in PROVIDERS.values() else 0
    chosen = st.selectbox("Provider", labels, index=idx, key="provider_select")
    new_key = PROVIDERS[chosen]

    # On provider change: reset llm so it’s rebuilt
    if new_key != st.session_state.provider_key:
        st.session_state.provider_key = new_key
        for k in ("llm", "llm_error"):
            st.session_state.pop(k, None)

    # Build llm when missing
    if "llm" not in st.session_state:
        llm, err = get_llm("groq")
        st.session_state.llm = llm
        st.session_state.llm_error = err

    if st.session_state.get("llm_error"):
        st.error(st.session_state.llm_error)
    else:
        st.success("Groq connected")

    st.divider()
    if st.button("Clear chat"):
        st.session_state.chat_history = []
        st.rerun()

    st.caption("Powered by Groq")

# --- Main chat ---
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    else:
        with st.chat_message("assistant"):
            st.write(message.content)

if st.session_state.get("llm") is None:
    st.info("Add your **GROQ_API_KEY** in `.env` file. Get a free key: [console.groq.com](https://console.groq.com)")

user_input = st.chat_input("Message")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if st.session_state.get("llm") is None:
                st.error(st.session_state.get("llm_error") or "Pick a model and add your free API key in the sidebar.")
                st.session_state.chat_history.pop()
            else:
                try:
                    # Ensure messages are in correct format
                    messages = st.session_state.chat_history.copy()
                    response = st.session_state.llm.invoke(messages)
                    
                    # Extract content from response
                    if hasattr(response, "content"):
                        reply = response.content
                    elif isinstance(response, str):
                        reply = response
                    else:
                        reply = str(response)
                    
                    # Check if reply is empty
                    if not reply or not reply.strip():
                        st.error("Received empty response from the model. Please try again.")
                        st.session_state.chat_history.pop()
                    else:
                        st.write(reply)
                        st.session_state.chat_history.append(AIMessage(content=reply))
                except Exception as e:
                    err = str(e).lower()
                    if "quota" in err or "429" in err or "limit" in err or "insufficient_quota" in err:
                        st.error("**Quota exceeded.** Try again later or check [console.groq.com](https://console.groq.com)")
                    elif "api_key" in err or "auth" in err or "401" in err:
                        st.error("Check your API key in `.env` and that it’s correct for the selected model.")
                    else:
                        # Show full error for debugging
                        st.error(f"**Error:** {str(e)}")
                        st.caption("If this persists, check your API key and account status.")
                    st.session_state.chat_history.pop()
