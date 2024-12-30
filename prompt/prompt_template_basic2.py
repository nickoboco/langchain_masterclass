from langchain.prompts import ChatPromptTemplate

# Define o template do prompt com múltiplos parâmetros
template_multiple = """Você é um assistente engraçado.
Me conte uma piada {adjective} sobre {topic}.
Assistente:"""

# Cria um prompt a partir do template
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)

# Invoca o prompt com os parâmetros definidos
prompt = prompt_multiple.invoke({'adjective': 'estranha', 'topic': 'computadores'})

print("\n----Prompt template----\n")
print(prompt)