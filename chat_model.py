from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

result = model.invoke('Quanto é 2 + 2?')

print("Full result:", result)
print("Content only:", result.content)