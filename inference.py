from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True).to('mps')
model = model.eval()

response, history = model.chat(tokenizer, '你好', history=[])

print(response)

response, history = model.chat(tokenizer, "睡不着怎么办")
print(response)
