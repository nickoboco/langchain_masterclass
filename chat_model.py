from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente
load_dotenv()

# Instancia o modelo de chat
model = ChatOpenAI(model='gpt-4o-mini')

# Faz uma pergunta ao modelo
result = model.invoke('Quanto é 2 + 2?')

# Exibe os resultados
print("Exemplo de retorno completo: ", result)
print("Exemplo de retorno somente com a resposta: ", result.content)