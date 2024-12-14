from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="D:/COURSES/New folder/.env")

api_key=os.getenv("API_KEY")

if __name__=='__main__':
    template = """ Translate the following text into {language}:{sentence} """
    prompt = PromptTemplate(
        input_variables=["sentence", "language"],
        template=template
    )
    llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=api_key)

    
chain = prompt| llm| StrOutputParser()

res=chain.invoke({"sentence":"hello i am devansh","language":"German"})
print(res)