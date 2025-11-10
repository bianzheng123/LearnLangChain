from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
import os

# 1. 初始化模型
# model = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    temperature=0.7
)

# 2. 调用 stream 方法并迭代输出
print("模型回答：", end="", flush=True)
for chunk in llm.stream("Why do parrots have colorful feathers?"):
    # 注意：这里应使用 chunk.content 而非 chunk.text
    print(chunk.content, end="", flush=True) # 使用空字符串 end="" 确保不换行