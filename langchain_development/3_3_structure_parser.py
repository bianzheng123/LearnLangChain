from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Optional
import os

# 使用Pydantic模型定义数据结构
class UserInfo(BaseModel):
    name: str = Field(description="用户的姓名")
    age: int = Field(description="用户的年龄")
    occupation: Optional[str] = Field(description="用户的职业", default=None)

# 创建Pydantic解析器
parser = PydanticOutputParser(pydantic_object=UserInfo)

model = init_chat_model(
    model='deepseek-chat',
    model_provider='deepseek',
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
)

prompt = PromptTemplate.from_template(
    "请根据以下内容提取用户信息：\n{input}\n\n{format_instructions}"
)

chain = (
    prompt.partial(format_instructions=parser.get_format_instructions())
    | model
    | parser
)

result = chain.invoke({"input": "用户叫李雷，今年25岁，是一名工程师。"})
print(result)