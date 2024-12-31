from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente e cria o modelo
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

# Função que conta as palavras de um texto - Exemplo de função intermediária
def func(x):
    cont_words = len(x.split())
    print(x)
    return f'\nO texto tem {cont_words} letras'

# Cria um template de prompt
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um comediante que conta piadas sobre {topic}."),
        ("user", "Conte {num_jokes} piadas."),
    ]
)

# Cria lambdas para executar operações específicas
# Ao estender uma chain, é possível adicionar lambdas intermediárias
uppercase_output = RunnableLambda(lambda x: x.upper())
count_words = RunnableLambda(func)

# Cria a chain de execução por meio de uma sequência e aciona a execução
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words
result = chain.invoke({"topic": "gatos", "num_jokes": 3})

print(result)