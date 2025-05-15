# Local Prompt Optimizer

A simple Streamlit web app that uses a local LLM (Mistral-7B) to enhance and optimize your prompts for better results with large language models.

## Features

- Runs entirely locally—no data leaves your machine.
- Uses the `llama_cpp` library to load and run the Mistral-7B model.
- User-friendly Streamlit interface for entering and optimizing prompts.

## Usage

1. Make sure you have Python 3.8+ installed.
2. Clone the repo, cd into the folder and create virtual python environment 
    > git clone https://github.com/florexong/Local_Prompt_Optimizer
    >
    > cd Local_Prompt_Optimizer
    >
    > python -m venv #change it to virtual environment name you want
3. Activate the python virtual environment and install the required dependencies 
    > venv\Scripts\activate
    >
    > pip install requirements.txt
4. Download the Mistral-7B model and place it in the `models/` directory.
    >Run it on powershell
    >
    >wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf
5. Run the app:
    > streamlit run app.py