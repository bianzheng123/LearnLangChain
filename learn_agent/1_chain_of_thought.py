from openai import OpenAI
from typing import List, Dict
import os

def ask(messages: List[Dict]):
        #需要指定api key 以及base_url
        client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
                model = 'deepseek-chat',
                temperature = 0,
                messages = messages
        )

        return response

system_prompt = """ 
    You are a helpful assistant.
"""

question = """Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
Each can has 3 tennis balls. How many tennis balls does he have now?
A: The answer is 11.
Q: The cafeteria had 23 apples.
If they used 20 to make lunch and bought 6 more, how many apples do they have?
A:"""