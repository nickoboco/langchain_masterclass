from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableBranch
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente e cria o modelo
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

# Cria os templates de prompt
prompt_template_positive = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente responsável por responder pesquisas de satisfação do nosso produto."),
        ("human", "Gere uma nota de agradecimento ao cliente para seguinte avaliação positiva: {review}."),
    ]
)

prompt_template_negative = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente responsável por responder pesquisas de satisfação do nosso produto."),
        ("human", "Gere uma nota de desculpas ao cliente para a avaliação negativa: {review}."),
    ]
)

prompt_template_neutral = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente responsável por responder pesquisas de satisfação do nosso produto."),
        ("human", "Gere uma nota de desculpas especulando melhor o motivo da seguinte avaliação neutra: {review}."),
    ]
)

prompt_template_escalate = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente responsável por responder pesquisas de satisfação do nosso produto."),
        ("human", "Gere uma nota de escalonamento para o atendimento interno para a seguinte avaliação: {review}."),
    ]
)

prompt_classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é responsável por classificar as pesquisas de satisfação."),
        ("human", "Classifique esse feedback como positivo, negativo, neutro ou escalado: {response}"),
    ]
)

# Cria a cadeia de execução avaliando a resposta do usuário
answer_chain = RunnableBranch(
    (
        lambda x: "positivo" in x.lower(),
        prompt_template_positive | model | StrOutputParser()
    ),
    (
        lambda x: "negativo" in x.lower(),
        prompt_template_negative | model | StrOutputParser()
    ),
    (
        lambda x: "neutro" in x.lower(),
        prompt_template_neutral | model | StrOutputParser()
    ),
    prompt_template_escalate | model | StrOutputParser() # Se não for nenhuma das anteriores, escalona
)

# Cria a cadeia de execução principal
classification_chain = prompt_classification_template | model | StrOutputParser()
main_chain = classification_chain | answer_chain

# Invoca a cadeia de execução
result = main_chain.invoke({"response": "Produto maravilhoso, estou muito satisfeito!"})

print(result)