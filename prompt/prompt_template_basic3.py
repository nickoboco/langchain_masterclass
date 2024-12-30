from langchain.prompts import ChatPromptTemplate

# Definindo mensagens com variáveis - Deve usar tuplas para definir as mensagens com variáveis
messages = [
    ("system", "Você é um comediante que conta piadas sobre {topic}."),
    ("user", "Conte {quantidade} piadas."),
]

# Criando um prompt template a partir das mensagens
prompt_template = ChatPromptTemplate.from_messages(messages)

# Invocando o prompt template com valores específicos
prompt = prompt_template.invoke({'topic': 'computadores', 'quantidade': 'duas'})

print("\n----Prompt template----\n")
print(prompt)