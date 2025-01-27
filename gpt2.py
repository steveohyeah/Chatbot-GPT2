import time
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from constants import NUM_SEQ, NNGRAN


# Upload model and tokenizer of GPT-2
@st.cache_resource
def load_gpt2():
    """Function that downloads the model and tokenizer if they are not in local cache"""
    loading_message = st.empty()
    loading_message.text("Charging model GPT-2...")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    loading_message.empty()
    return model, tokenizer


# Generate response
def response_gpt2(model, tokenizer, input, ilength, itemperature, itop_p, logger):
    """Function that generates response, saves loggings and the conversation in the history and verify if the input and the response generation are correct"""
    if input:
        st.session_state["conversation"].append({"user": input})
        logger.info(f"Usuario: {input}")
        inputs = tokenizer.encode(input, return_tensors="pt")
        try:
            start_time = time.time()
            outputs = model.generate(
                inputs,
                max_length=ilength,
                temperature=itemperature,
                top_p=itop_p,
                num_return_sequences=NUM_SEQ,
                no_repeat_ngram_size=NNGRAN,
            )
            end_time = time.time()
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Add bot response to conversation history
            st.session_state["conversation"].append({"bot": generated_text})

            logger.info(f"Bot: {generated_text}")
            logger.info(
                f"Tiempo de generación de respuesta: {end_time - start_time:.2f} segundos"
            )

            return generated_text
        except Exception as e:
            return f"Error al generar la respuesta: {e}"
    else:
        st.warning("Please, write something before continuing.")
