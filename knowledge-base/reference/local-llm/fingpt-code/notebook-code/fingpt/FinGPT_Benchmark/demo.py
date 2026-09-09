# Research reading export only; notebook cells not executed.

# First choose to load data/model from huggingface or local space

FROM_REMOTE = False

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from utils import *

import logging
# Suppress Warnings during inference
logging.getLogger("transformers").setLevel(logging.ERROR)

demo_tasks = [
    'Financial Sentiment Analysis',
    'Financial Relation Extraction',
    'Financial Headline Classification',
    'Financial Named Entity Recognition',
]
demo_inputs = [
    "Glaxo's ViiV Healthcare Signs China Manufacturing Deal With Desano",
    "Wednesday, July 8, 2015 10:30AM IST (5:00AM GMT) Rimini Street Comment on Oracle Litigation Las Vegas, United States Rimini Street, Inc., the leading independent provider of enterprise software support for SAP AG’s (NYSE:SAP) Business Suite and BusinessObjects software and Oracle Corporation’s (NYSE:ORCL) Siebel , PeopleSoft , JD Edwards , E-Business Suite , Oracle Database , Hyperion and Oracle Retail software, today issued a statement on the Oracle litigation.",
    'april gold down 20 cents to settle at $1,116.10/oz',
    'Subject to the terms and conditions of this Agreement , Bank agrees to lend to Borrower , from time to time prior to the Commitment Termination Date , equipment advances ( each an " Equipment Advance " and collectively the " Equipment Advances ").',
]
demo_instructions = [
    'What is the sentiment of this news? Please choose an answer from {negative/neutral/positive}.',
    'Given phrases that describe the relationship between two words/phrases as options, extract the word/phrase pair and the corresponding lexical relationship between them from the input text. The output format should be "relation1: word1, word2; relation2: word3, word4". Options: product/material produced, manufacturer, distributed by, industry, position held, original broadcaster, owned by, founded by, distribution format, headquarters location, stock exchange, currency, parent organization, chief executive officer, director/manager, owner of, operator, member of, employer, chairperson, platform, subsidiary, legal form, publisher, developer, brand, business division, location of formation, creator.',
    'Does the news headline talk about price in the past? Please choose an answer from {Yes/No}.',
    'Please extract entities and their types from the input sentence, entity types should be chosen from {person/organization/location}.',
]

def load_model(base_model, peft_model, from_remote=False):
    
    model_name = parse_model_name(base_model, from_remote)

    model = AutoModelForCausalLM.from_pretrained(
        model_name, trust_remote_code=True, 
        device_map="auto",
    )
    model.model_parallel = True

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    
    tokenizer.padding_side = "left"
    if base_model == 'qwen':
        tokenizer.eos_token_id = tokenizer.convert_tokens_to_ids('<|endoftext|>')
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids('<|extra_0|>')
    if not tokenizer.pad_token or tokenizer.pad_token_id == tokenizer.eos_token_id:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        model.resize_token_embeddings(len(tokenizer))
    
    model = PeftModel.from_pretrained(model, peft_model)
    model = model.eval()
    return model, tokenizer


def test_demo(model, tokenizer):

    for task_name, input, instruction in zip(demo_tasks, demo_inputs, demo_instructions):
        prompt = 'Instruction: {instruction}\nInput: {input}\nAnswer: '.format(
            input=input, 
            instruction=instruction
        )
        inputs = tokenizer(
            prompt, return_tensors='pt',
            padding=True, max_length=512,
            return_token_type_ids=False
        )
        inputs = {key: value.to(model.device) for key, value in inputs.items()}
        res = model.generate(
            **inputs, max_length=512, do_sample=False,
            eos_token_id=tokenizer.eos_token_id
        )
        output = tokenizer.decode(res[0], skip_special_tokens=True)
        print(f"\n==== {task_name} ====\n")
        print(output)
    

base_model = 'llama2'
peft_model = 'FinGPT/fingpt-mt_llama2-7b_lora' if FROM_REMOTE else 'finetuned_models/MT-llama2-linear_202309241345'

model, tokenizer = load_model(base_model, peft_model, FROM_REMOTE)
test_demo(model, tokenizer)

base_model = 'qwen'
peft_model = 'FinGPT/fingpt-mt_qwen-7b_lora' if FROM_REMOTE else 'finetuned_models/MT-qwen-linear_202309221011'

model, tokenizer = load_model(base_model, peft_model, FROM_REMOTE)
test_demo(model, tokenizer)

base_model = 'falcon'
peft_model = 'FinGPT/fingpt-mt_falcon-7b_lora' if FROM_REMOTE else 'finetuned_models/MT-falcon-linear_202309210126'

model, tokenizer = load_model(base_model, peft_model, FROM_REMOTE)
test_demo(model, tokenizer)

base_model = 'chatglm2'
peft_model = 'FinGPT/fingpt-mt_chatglm2-6b_lora' if FROM_REMOTE else 'finetuned_models/MT-chatglm2-linear_202309201120'

model, tokenizer = load_model(base_model, peft_model, FROM_REMOTE)
test_demo(model, tokenizer)

base_model = 'bloom'
peft_model = 'FinGPT/fingpt-mt_bloom-7b1_lora' if FROM_REMOTE else 'finetuned_models/MT-bloom-linear_202309211510'

model, tokenizer = load_model(base_model, peft_model, FROM_REMOTE)
test_demo(model, tokenizer)

base_model = 'mpt'
peft_model = 'FinGPT/fingpt-mt_mpt-7b_lora' if FROM_REMOTE else 'finetuned_models/MT-mpt-linear_202309230221'

model, tokenizer = load_model(base_model, peft_model, FROM_REMOTE)
test_demo(model, tokenizer)
