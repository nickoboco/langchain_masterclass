from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Carrega as variáveis de ambiente
load_dotenv()

# Cria o modelo de chat
model = ChatOpenAI(model='gpt-4o-mini')

# Define as lista vazia para adicionar mensagens
chat_history = []

# Adiciona a mensagem do sistema
system_message = SystemMessage(content='Você é um assistente de TI.')

# Adiciona a mensagem do sistema ao histórico
chat_history.append(system_message)

# Loop para conversar com o usuário
while True:
    # Pergunta ao usuário
    query = input('Você: ')

    # Verifica se o usuário deseja sair
    if query.lower() == 'sair':
        break
    
    # Adiciona a mensagem do usuário ao histórico
    chat_history.append(HumanMessage(content=query))

    # Invoca o modelo de chat
    result = model.invoke(chat_history)

    # Obtém a resposta da IA
    response = result.content

    # Adiciona a mensagem da IA ao histórico
    chat_history.append(AIMessage(content=response))

    # Exibe a resposta da IA
    print(f'AI: {response}')

# Exibe o histórico de mensagens no fim da conversa - Fim didático
print("Histórico de Mensagens")
print(chat_history)