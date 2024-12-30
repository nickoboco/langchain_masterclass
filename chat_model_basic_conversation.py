from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente
load_dotenv()

# Cria o modelo de chat
model = ChatOpenAI(model='gpt-4o-mini')

# Define as mensagens de entrada
messages = [
    # Mensagem do sistema
    SystemMessage(content='Especialista em matemática'),
    # Mensagem do usuário
    HumanMessage(content='Quanto é 2 + 2?'),
]

# Invoca o modelo de chat
result = model.invoke(messages)

# Exibe a resposta da IA
print(f'Resposta da IA: {result.content}')

# Define as mensagens de entrada adicionando histórico da conversa manualmente
messages = [
    # Mensagem do sistema
    SystemMessage(content='Especialista em matemática'),
    # Mensagem do usuário
    HumanMessage(content='Quanto é 2 + 2?'),
    # Mensagem do sistema
    AIMessage(content='A soma de 2 + 2 é 4.'),
    # Mensagem do usuário
    HumanMessage(content='Quando é 3 * 3?'),
]

# Invoca o modelo de chat
result = model.invoke(messages)

# Exibe a resposta da IA
print(f'Resposta da IA: {result.content}')