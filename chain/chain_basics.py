from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

# Carrega as variáveis de ambiente e cria o modelo
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

# Cria um template de prompt
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um comediante que conta piadas sobre {topic}."),
        ("user", "Conte {num_jokes} piadas."),
    ]
)

# Cria a cadeia de execução e invoca o modelo
# O resultado é um objeto do tipo str
chain = prompt_template | model | StrOutputParser()
result = chain.invoke({"topic": "computadores", "num_jokes": 3})

print(result)