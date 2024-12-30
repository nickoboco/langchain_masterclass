from dotenv import load_dotenv
from google.auth import compute_engine
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa as variáveis do firebase
PROJECT_ID = os.getenv("PROJECT_ID")
SESSION_ID = "user2_session"
COLLECTION_NAME = "chat_history"

# Inicializa o Firestore Client
print("Inicializando Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Inicializa o Firestore Chat Message History
print("Inicializando Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

# Inicializa o histórico de Chat
print('Histórico de Chat inicializado com sucesso!')
print('Histórico de Chat:', chat_history.messages)

# Inicializa o Chat Model
model = ChatOpenAI(model='gpt-4o-mini')

# Inicia o Chat
print('Chat iniciando com IA. Digite "sair" para encerrar o chat.')
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        break
    
    chat_history.add_user_message(user_input)
    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f'AI: {ai_response.content}')