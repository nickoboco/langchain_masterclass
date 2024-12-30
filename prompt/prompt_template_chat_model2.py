from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente
load_dotenv()

# Cria o modelo de chat
model = ChatOpenAI(model='gpt-4o-mini')

print("\n----Prompt a partir de um template----\n")

# Define o template do prompt com múltiplos parâmetros
template_multiple = """Você é um assistente engraçado.
Me conte uma piada {adjective} sobre {topic}.
Assistente:"""

# Cria um prompt a partir do template
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)

# Invoca o prompt com os parâmetros definidos
prompt = prompt_multiple.invoke({'adjective': 'estranha', 'topic': 'computadores'})

# Invoca o modelo de chat com o prompt
result = model.invoke(prompt)
print(result.content)