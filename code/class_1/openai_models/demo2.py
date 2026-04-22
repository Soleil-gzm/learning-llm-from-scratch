# 需求： 1、先创建一个向量空间
#       2、根据一个给定的句子，去向量空间中做搜索，找到最相似的句子
#       3、计算相似度
# 步骤： 1、准备数据，并读取

from turtle import pd
from openai import OpenAI

df = pd.read_csv('datas/fine_food_reviews_1k.csv',index_col=0)

df = df[['Time','ProductId','Score','Summary','Text']]

# 2、清洗数据
df.dropna()
df['text_content'] = 'Summary:'+df.Summary.str.strip() + '; Text:' + df.Text.str.strip()

print(df.head(2))

# 3、创建向量空间

client =OpenAI(
    base_url="https://xiaoai.pluss/v1",
    api_key='sk-doD81WgxSoF9A6xYzhgW7GUh5frRwPETI8mDq#ce4UaWnCPF'
)

def text_to_embedding(text,model):
    return client.embeddings.create(input=text,model=model).data[0].embedding

# 4、把text_content字段的文本值转换成向量，并存储在新字段'embedding'中
df['embedding'] = df.text_content.apply(lambda x: text_to_embedding(x,'text-embedding-3-small'))

# 5、把结果保存到本地文件中
df.to_csv('datas/output_embedding.csv')