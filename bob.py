from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answearing import load_qa_chain
from langchain.llms import OpenAI

# Initialize your components here
chave_openai = ''

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=24,
    length_function=count_tokens,
)

# Assume text is loaded and processed here
with open('bob.txt', 'r', encoding="utf-8") as f:
    text = f.read()

chunks = text_splitter.create_documents([text])

embeddings = OpenAIEmbeddings(openai_api_key=chave_openai, model="text-embedding-ada-002")
db = FAISS.from_documents(chunks, embeddings)

def process_query(query):
    docs = db.similarity_search(query)
    chain = load_qa_chain(OpenAI(openai_api_key=chave_openai, temperature=0.7), chain_type="stuff")
    answer = chain.run(input_documents=docs, question=query)
    return answer
