from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente
load_dotenv()

# Cria o modelo de chat
model = ChatOpenAI(model='gpt-4o-mini')

print("\n----Prompt a partir de um template----\n")

# Definindo mensagens com variáveis - Deve usar tuplas para definir as mensagens com variáveis
messages = [
    ("system", "Você é um comediante que conta piadas sobre {topic}."),
    ("user", "Conte {quantidade} piadas."),
]

# Criando um prompt template a partir das mensagens
prompt_template = ChatPromptTemplate.from_messages(messages)

# Invocando o prompt template com valores específicos
prompt = prompt_template.invoke({'topic': 'computadores', 'quantidade': '2'})

# Invocando o modelo de chat com o prompt
result = model.invoke(prompt)
print(result.content)