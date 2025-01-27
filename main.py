import streamlit as st
import gpt2
import log_history
import st_funct


if __name__ == "__main__":

    # Create logging var
    logger = log_history.log_conf()

    # Initialize model and tokenizer
    model, tokenizer = gpt2.load_gpt2()

    # Initialize session state for context/history
    st_funct.session_history()

    # Botchat with streamlit
    input, length, temperature, top = st_funct.streamlit_config()

    # Button to generate the answer
    st_funct.button_generation(
        model, tokenizer, input, length, temperature, top, logger
    )

    # Display conversation history
    st_funct.conversation_history()
