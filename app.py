import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "deepseek-ai/deepseek-coder-1.3b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)

def generate_response(user_input):
    prompt = f"### Instruction:\n{user_input}\n\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output_text.replace(prompt, "").strip()

# Streamlit UI
st.set_page_config(page_title="📜 Law Chatbot", layout="centered")
st.title("🧑‍⚖️ Legal Assistant")
st.markdown("Ask me any legal question related to FIRs, criminal law, or general legal procedure.")

question = st.text_input("📝 Type your legal question below:")

if question:
    with st.spinner("Analyzing..."):
        answer = generate_response(question)
        st.success("🤖 " + answer)
