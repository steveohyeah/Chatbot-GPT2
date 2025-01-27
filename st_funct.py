import streamlit as st
import gpt2
from constants import (
    MAX_LENGTH,
    MIN_LENGTH,
    VAL_LENGTH,
    MAX_TEMP,
    MIN_TEMP,
    VAL_TEMP,
    STP_TEMP,
    MAX_TOP,
    MIN_TOP,
    VAL_TOP,
    STP_TOP,
)


# Initialize session state for context/history
def session_history():
    """Function that initializeS session state for context/history"""
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []  # Stores history of interactions


def streamlit_config():
    """Fuction that prepares all the components in the streamlit page"""
    # Title
    st.title("Botchat gpt2")

    # Text input user
    user_input = st.text_area("Write your question:")

    # Generation params configuration
    max_length = st.slider(
        "Length of the generated text:",
        min_value=MIN_LENGTH,
        max_value=MAX_LENGTH,
        value=VAL_LENGTH,
    )
    temperature = st.slider(
        "Temperature:",
        min_value=MIN_TEMP,
        max_value=MAX_TEMP,
        value=VAL_TEMP,
        step=STP_TEMP,
    )
    top_p = st.slider(
        "Top-p (nucleus sampling):",
        min_value=MIN_TOP,
        max_value=MAX_TOP,
        value=VAL_TOP,
        step=STP_TOP,
    )
    return user_input, max_length, temperature, top_p


def button_generation(model, tokenizer, input, length, temperature, top, logger):
    """Button that generates the answer and the display of it"""
    if st.button("Generate text"):
        response = gpt2.response_gpt2(
            model, tokenizer, input, length, temperature, top, logger
        )

        # Display the generated text
        st.markdown(f"### Response:")
        st.write(response)


def conversation_history():
    """Function that displays conversation history"""
    st.subheader("Conversation History:")
    for message in st.session_state["conversation"]:
        if "user" in message:
            st.write(f"**User:** {message['user']}")
        if "bot" in message:
            st.write(f"**Bot:** {message['bot']}")
