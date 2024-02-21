import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown
from langchain.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv
import openai


load_dotenv() # loads the env
openai.api_key = os.environ["OPENAI_API_KEY"]
# huggingfacehub_api_key = os.environ["HUGGINGFACEHUB_API_KEY"]
# serpapi_api_key = os.environ["SERPAPI_API_KEY"]

if openai.api_key is None:
    raise ValueError("OPENAI API KEY is not set in the environment.")
