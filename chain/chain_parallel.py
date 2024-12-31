from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente e cria o modelo
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

# Cria um template de prompt
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um avaliador de produtos especialista."),
        ("human", "Liste as 5 principiais características do produto {product}."),
    ]
)

# Funções para analisar os prós e contras
def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um especialista em produtos."),
            (
                "human",
                "Considerando as features: {features}, liste os prós dessas features." 
            ),
        ]
    )
    return pros_template.format_prompt(features=features)


def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um especialista em produtos."),
            (
                "human",
                "Considerando as features: {features}, liste os contras dessas features." 
            ),
        ]
    )
    return cons_template.format_prompt(features=features)

# Função para combinar os prós e contras
def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"

# Cria as chains para pros e cons
pros_branch_chain = (
    RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser()
)

cons_branch_chain = (
    RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
)

# Cria a chain principal
chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain}) # Cria um dicionario com as branches paralelas
    | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"])) # Combina os resultados das branches
)

# Executa a chain
result = chain.invoke({"product": "Celular"})

print(result)