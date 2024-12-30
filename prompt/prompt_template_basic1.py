from langchain.prompts import ChatPromptTemplate

# Define a template simples
template = 'Me conte uma piada sobre {topic}.'

# Cria um objeto ChatPromptTemplate a partir do template
prompt_template = ChatPromptTemplate.from_template(template)

print("\n----Prompt template----\n")

# Invoca o template com o argumento 'topic' definido
prompt = prompt_template.invoke({'topic': 'computadores'})

print(prompt)