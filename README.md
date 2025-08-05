# 🧠 DeepSeek Coder 1.3B – Fine-Tuned Lawyer Chatbot using LoRA

This project implements a legal assistant chatbot by fine-tuning the DeepSeek Coder 1.3B model using the LoRA (Low-Rank Adaptation) technique. The chatbot is trained on a custom dataset of legal questions and answers.

## 🔍 Features

- ✅ Fine-tuning using LoRA for lightweight training
- ✅ Base model: [DeepSeek Coder 1.3B Instruct](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct)
- ✅ 8-bit quantization to reduce memory usage
- ✅ Custom instruction-response format dataset
- ✅ Easy inference with `ask()` function
- ✅ Compatible with Google Colab & Hugging Face Transformers

## 📁 Repository Structure

| File/Folder            | Description                                 |
|------------------------|---------------------------------------------|
| `app.py`               | Script to run and test chatbot              |
| `lawyer_data.jsonl`    | Training dataset in instruction format      |
| `deepseek_lawyer/`     | Saved LoRA adapter and tokenizer files      |
| `requirements.txt`     | Python dependencies for the project         |
| `notebook.ipynb`       | Full training notebook (Colab ready)        |

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ayesha-code1811/Fine-Tuning-DeepSeek-Coder-1.3B-for-Lawyer-Chatbot-using-LoRA.git

## 🛠 Technologies Used
DeepSeek Coder 1.3B

Hugging Face Transformers

PEFT (LoRA)

Datasets (JSONL)

Python & PyTorch

Google Colab
