# 先安装专用包（如果可用）
# pip install langchain-deepseek

from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek  # 或从相应包导入
import os

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 使用DeepSeek专用类
llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.environ.get('DEEPSEEK_API_KEY'),  # 替换为你的API密钥
    temperature=0.7
)


agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

res = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(res)