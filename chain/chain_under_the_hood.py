from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
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

# Cria a cadeia de execução por meio de lambdas
# Cada lambda é uma função que recebe um objeto e retorna um objeto
# O objeto de entrada é o resultado da execução anterior
# O objeto de saída é o resultado da execução atual
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Cria a chain de execução por meio de uma sequência
# A sequência é composta por uma função inicial, uma lista de funções intermediárias e uma função final
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Invoca a cadeia de execução
result = chain.invoke({"topic": "computadores", "num_jokes": 3})

print(result)