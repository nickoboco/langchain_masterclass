import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Definir o caminho para o arquivo de texto e chroma_db
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'books', 'titanic.txt')
persistent_directory = os.path.join(current_dir, 'db', 'chroma_db')

if not os.path.exists(persistent_directory):
    print('Diretório de banco de dados não encontrado. Criando Vector Database...')

    # Carregar o arquivo de texto
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f'Arquivo de texto não encontrado em {file_path}'
        )
    
    # Carregar o arquivo de texto
    loader = TextLoader(file_path, encoding='utf-8')
    documents = loader.load()

    # Dividir o texto em chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    print("\n--- Documentos divididos ---")
    print(f"Total de documentos: {len(docs)}")
    print(f"Exemplo de chunk:\n{docs[0].page_content}\n")

    #Criar embeddings
    print("\n--- Criando embeddings ---")
    embeddings = OpenAIEmbeddings(
        model='text-embedding-3-small'
    )
    print('\n--- Embeddings criados ---')

    # Criar Vector Store
    print("\n--- Criando Vector Store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Vector Store criado ---")

else:
    print('Vector Database encontrado em', persistent_directory)

