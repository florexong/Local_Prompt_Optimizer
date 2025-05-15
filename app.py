import streamlit as st
from llama_cpp import Llama

## change the model path in case the model is different
MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

@st.cache_resource
def load_llm():
    return Llama(
        model_path=MODEL_PATH,
        n_gpu_layers=35,
        n_ctx=2048,
        use_mlock=True,
        use_mmap=False,
    )

llm = load_llm()

def enhance_prompt(user_prompt):
    system_prompt = "You are a prompt engineer assistant. Given a vague user request, improve it to be detailed, clear, and well-structured for LLM use."
    full_prompt = f"[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\nUser input: {user_prompt}\nImproved prompt: [/INST]"
    output = llm(full_prompt, temperature=0.7, max_tokens=512, stop=["</s>"])
    return output["choices"][0]["text"].strip()

st.title("🎯 Prompt Optimizer Agent")
user_input = st.text_area("💬 Enter your vague or rough prompt:", height=150)

if st.button("Optimize Prompt"):
    with st.spinner("Enhancing your prompt with local LLM..."):
        optimized = enhance_prompt(user_input)
        st.success("Optimized Prompt Generated!")
        st.text_area("🧠 Refined Prompt", optimized, height=200)