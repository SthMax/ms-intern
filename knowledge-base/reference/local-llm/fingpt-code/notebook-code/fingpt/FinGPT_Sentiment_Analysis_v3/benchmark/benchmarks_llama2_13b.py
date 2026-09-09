# Research reading export only; notebook cells not executed.

import sys
sys.path.append('/mnt/c/Users/Olive/python_projects/FinNLP/FinNLP')  # https://github.com/AI4Finance-Foundation/FinNLP

# only for WSL
import os 
os.environ["PATH"] = f"{os.environ['PATH']}:/usr/local/cuda-12.0/bin"
# os.environ['LD_LIBRARY_PATH'] = "/usr/lib/wsl/lib:/usr/local/cuda/lib64"
os.environ['LD_LIBRARY_PATH'] = "/usr/local/cuda-12.0/lib64"
os.environ["BNB_CUDA_VERSION"]="120"

from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM, LlamaForCausalLM, LlamaTokenizerFast   # 4.30.2
from peft import PeftModel  # 0.4.0
import torch

from finnlp.benchmarks.fpb import test_fpb
from finnlp.benchmarks.fiqa import test_fiqa , add_instructions
from finnlp.benchmarks.tfns import test_tfns
from finnlp.benchmarks.nwgi import test_nwgi

# # v3.1
# base_model = "THUDM/chatglm2-6b"
# peft_model = "oliverwang15/FinGPT_v31_ChatGLM2_Sentiment_Instruction_LoRA_FT"
# tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
# model = AutoModel.from_pretrained(base_model, trust_remote_code=True, load_in_8bit = True, device_map = "auto")
# model = PeftModel.from_pretrained(model, peft_model)
# model = model.eval()

# v3.2
# base_model = "meta-llama/Llama-2-7b-chat-hf"  # Access needed
base_model = "NousResearch/Llama-2-13b-hf" 
peft_model = "oliverwang15/FinGPT_v33_Llama2_13B_Sentiment_Instruction_LoRA_FT_8bit"
tokenizer = LlamaTokenizerFast.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
model = LlamaForCausalLM.from_pretrained(base_model, trust_remote_code=True, device_map = "cuda:0", load_in_8bit = True,)
model = PeftModel.from_pretrained(model, peft_model)
model = torch.compile(model)  # Please comment this line if your platform does not support torch.compile
model = model.eval()

batch_size = 16

# FPB
res = test_fpb(model, tokenizer, batch_size = batch_size)

def pf(x):
    return  "What is the sentiment of this news? Please choose an answer from {strong negative/moderately negative/mildly negative/neutral/mildly positive/moderately positive/strong positive}, then provide some short reasons."

# FiQA
res = test_fiqa(model, tokenizer, prompt_fun = add_instructions, batch_size = batch_size)
# res = test_fiqa(model, tokenizer, batch_size = batch_size, prompt_fun=pf)

# TFNS
res = test_tfns(model, tokenizer, batch_size = batch_size)

# NWGI
res = test_nwgi(model, tokenizer, batch_size = batch_size)
