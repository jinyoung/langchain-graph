
from langchain_experimental.graph_transformers.diffbot import DiffbotGraphTransformer

# diffbot_api_key = "42589433beee498941e0e8af31b8c4ce"
# diffbot_nlp = DiffbotGraphTransformer(diffbot_api_key=diffbot_api_key)

# from langchain.document_loaders import WikipediaLoader

# query = "Warren Buffett"
# raw_documents = WikipediaLoader(query=query).load()
# graph_documents = diffbot_nlp.convert_to_graph_documents(raw_documents)


from langchain.graphs import Neo4jGraph

url = "bolt://localhost:7687"
username = "neo4j"
password = "pleaseletmein"

graph = Neo4jGraph(url=url, username=username, password=password)



# graph.add_graph_documents(graph_documents)
#graph.refresh_schema()

from langchain.chains import GraphCypherQAChain
from langchain.chat_models import ChatOpenAI

chain = GraphCypherQAChain.from_llm(
    cypher_llm=ChatOpenAI(temperature=0, model_name="gpt-4"),
    qa_llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
    graph=graph,
    verbose=True,
)

chain.run("Which university did Warren Buffett attend?")

