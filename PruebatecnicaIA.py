import streamlit as st
import openai
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def load_model():
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer


def generate_query(prompt):
    messages = [
        {
            "role": "system",
            "content": f"Dame todo en formato json",
        },  # Intrucción inicial, se define como se quiere que responda el asistente
        {
            "role": "user",
            "content": prompt,
        },  # A nivel de usuario el qué tiene que responder
    ]

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Cambiar el modelo que se quiera
            messages=messages,  # Se mete todos los mensajes tanto de sistemas como de usuario
        )
        return completion.choices[0].message[
            "content"
        ]  # Hay varias elecciones de respuesta pero al querer la mejor es el 0
    except Exception as e:
        return f"Error al generar la respuesta: {e}"


st.title("Prueba técnica IA")

user_query = st.text_area("Escribe tu consulta:")

if st.button("Generar Respuesta"):
    if user_query:
        response = generate_query(user_query)
        st.markdown(f"### Respuesta:")
        st.write(response)
    else:
        st.warning("Por favor, escribe una consulta antes de continuar.")
