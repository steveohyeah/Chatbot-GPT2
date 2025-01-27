# Chatbot-GPT2
Chatbot GPT2 with streamlit and transformers

This project implements a text completion system using a pre-trained GPT-2 model from Hugging Face. The system includes the use of steamlit to manage the model and allow users to generate text completions based on user-provided prompts.

## **Features**

- Generate text completions based on a user-provided prompt.
- Customize parameters such as:
  - Maximum text length.
  - Temperature (creativity level).
  - Top-p (nucleus sampling).
- Input validation to ensure prompts are valid (non-empty strings).
- Logs to track requests and completions.

### **Access the Application**

Click on the following link to use the application:
👉 [Open the application in Streamlit](https://chatbot-gpt2-test.streamlit.app/)
Visit the application to generate text completions. Enter a prompt, and the GPT-2 model will complete your text based on the provided input and parameters.


## **Installing Instructions**

### **Requirements**
Developed in anaconda virtual environment. List of dependencies:
🔲**Python version** -> 3.11.8
🔲**Streamlit** -> 1.41.1
🔲**Transformers** -> 4.48.1
🔲**Torch** -> 2.5.1

1. **Clone the repository**:
   git clone https://github.com/steveohyeah/Chatbot-GPT2.git
   cd <repository-name>
2. **Create a virtual environment**:
   conda create -n <name_env> python=3.11.8
   conda activate <name_env>
3. **Install dependencies**:
   pip install -r requirements.txt
4. **Run the application**:
   ❗❗❗python -m streamlit run main.py❗❗❗
5. **Access Streamlit**:
   Open your browser at http://localhost:8501

## **Project Structure**
- **main.py**: Entry point for running the Streamlit application.
- **st_funct.py**: Streamlit functions.
- **gpt2.py**: Model loading and text generation logic.
- **log_history.py**: Logging configuration.
- **constants.py**: Constants for model and Streamlit configurations.
