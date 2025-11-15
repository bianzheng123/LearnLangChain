from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
import os


chatbot_prompt = ChatPromptTemplate.from_messages([
    ("system", "你叫苍井空，是日本著名女演员。"),
    ("user", "{input}")
])

# 使用 硅基流动 模型
model = init_chat_model(
    model='deepseek-chat',
    model_provider='deepseek',
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
)

# 直接使用模型 + 输出解析器
basic_qa_chain = chatbot_prompt | model | StrOutputParser()

# 测试
question = "你好，你演过多少作品"
result = basic_qa_chain.invoke(question)
print(result)