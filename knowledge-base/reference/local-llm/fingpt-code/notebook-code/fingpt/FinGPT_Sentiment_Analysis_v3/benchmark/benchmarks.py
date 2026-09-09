# Research reading export only; notebook cells not executed.

import sys
sys.path.append('../../../FinNLP/')  # https://github.com/AI4Finance-Foundation/FinNLP

from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM, LlamaForCausalLM, LlamaTokenizerFast   # 4.30.2
from peft import PeftModel  # 0.4.0
import torch

from finnlp.benchmarks.fpb import test_fpb
from finnlp.benchmarks.fiqa import test_fiqa , add_instructions
from finnlp.benchmarks.tfns import test_tfns
from finnlp.benchmarks.nwgi import test_nwgi

# v3.1
base_model = "THUDM/chatglm2-6b"
peft_model = "oliverwang15/FinGPT_v31_ChatGLM2_Sentiment_Instruction_LoRA_FT"
tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
model = AutoModel.from_pretrained(base_model, trust_remote_code=True, load_in_8bit = True, device_map = "auto")
model = PeftModel.from_pretrained(model, peft_model)
model = model.eval()

# v3.2
# base_model = "meta-llama/Llama-2-7b-chat-hf"  # Access needed
base_model = "daryl149/llama-2-7b-chat-hf"   
peft_model = "oliverwang15/FinGPT_v32_Llama2_Sentiment_Instruction_LoRA_FT"
tokenizer = LlamaTokenizerFast.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
model = LlamaForCausalLM.from_pretrained(base_model, trust_remote_code=True, device_map = "cuda:0")
model = PeftModel.from_pretrained(model, peft_model)
model = torch.compile(model)  # Please comment this line if your platform does not support torch.compile
model = model.eval()

batch_size = 8

# FPB
res = test_fpb(model, tokenizer, batch_size = batch_size)

# FiQA
res = test_fiqa(model, tokenizer, prompt_fun = add_instructions, batch_size = batch_size)

# TFNS
res = test_tfns(model, tokenizer, batch_size = batch_size)

# NWGI
res = test_nwgi(model, tokenizer, batch_size = batch_size)


