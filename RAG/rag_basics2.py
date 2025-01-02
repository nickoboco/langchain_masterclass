import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Definir o caminho para o chroma_db
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, 'db', 'chroma_db')

# Carregar modelo de embeddings
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

# Definir Vector Store
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Consulta
query = "number of passagers in the titanic"

# Criar o retriever
retriver = db.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3, 'fetch_k':5},
)

# Realizar a consulta
relevant_docs = retriver.invoke(query)

# Exibir os documentos relevantes
print("\n--- Documentos relevantes ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f'Documento {i}:\n{doc.page_content}\n')
    if doc.metadata:
        print(f'Fonte: {doc.metadata.get('source', 'desconhecido')}\n')