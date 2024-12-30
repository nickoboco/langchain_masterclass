from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente
load_dotenv()

# Cria o modelo de chat
model = ChatOpenAI(model='gpt-4o-mini')

print("\n----Prompt a partir de um template----\n")

# Cria um template de prompt com um parâmetro
template = "Me conte uma piada sobre {topic}"

# Cria um objeto de template de prompt
prompt_template = ChatPromptTemplate.from_template(template)

# Invoca o template de prompt com um valor para o parâmetro'
prompt = prompt_template.invoke({"topic": "computadores"})

# Invoca o modelo de chat com o prompt
result = model.invoke(prompt)

print(result.content)