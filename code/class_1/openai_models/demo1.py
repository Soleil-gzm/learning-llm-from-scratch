from openai import OpenAI

client =OpenAI(
    base_url="https://xiaoai.pluss/v1",
    api_key='sk-doD81WgxSoF9A6xYzhgW7GUh5frRwPETI8mDq#ce4UaWnCPF'

)
resp = client.embeddings.create(  # 发送请求
    model="text-embedding-3-small",
    input=" 我喜欢ai大模型"
    dimensions=1024
)

print(resp.data[0].embedding)
print(len(resp.data[0].embedding))

