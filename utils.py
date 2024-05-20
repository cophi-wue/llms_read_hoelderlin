from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama    
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai
import definitions as d
import os
import warnings

warnings.filterwarnings("ignore")

openaikey = ""
googlekey = ""
anthropickey = ""

#Google Gemini 
#model names: gemini-1.0-pro-latest gemini-1.5-pro-latest gemini-1.5-flash-latest
#@FIXME add temperature

def gemini(prompt):
    response = google_model.generate_content(prompt)
    return response.text
    
#ollama not directly supported in jupyter-ai, so we need this custom function.
#easy to adapt to other models than llama-3
#llama3:8b llama3:70b
def ollama3(model, temperature):
    llm = Ollama(model = model,
                temperature = temperature )

    prompt = PromptTemplate(
        input_variables=["question"],
        template="Answer the following question truthfully and concice. {question}",
    )
    return LLMChain(llm=llm, prompt=prompt)


#let us also use the new gpt4o model

def gpt4(temperature=0.8):
    llm = ChatOpenAI(
        model_name = 'gpt-4o',
        api_key = openaikey
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert in German literature. You answer the questions truthfully and short."),
        ("human", "{question}"),
    ])
    return LLMChain(llm=llm, prompt=prompt)
    

#opus can be registered directly in the notebook
#%ai register opus anthropic-chat:claude-3-opus-20240229 
# %ai register sonnet anthropic-chat:claude-3-sonnet-20240229 
#%ai register haiku anthropic-chat:claude-3-haiku-20240307 

###############
with open('openai_key.txt') as filein:
    openaikey = filein.read()
os.environ['OPENAI_API_KEY'] = openaikey

with open('google_key.txt') as filein:
    googlekey = filein.read()
os.environ['GOOGLE_API_KEY'] = googlekey

with open('anthropic_key.txt') as filein:
    anthropickey = filein.read()
os.environ['ANTHROPIC_API_KEY'] = anthropickey


#google gemini
genai.configure(api_key=googlekey)
google_model = genai.GenerativeModel('gemini-1.5-pro-latest') # gemini-1.0-pro-latest gemini-1.5-pro-latest gemini-1.5-flash-latest


