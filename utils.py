from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama    
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai
import os
import warnings

from IPython.display import Markdown, display


warnings.filterwarnings("ignore")

class Configuration:
    openaikey = ""
    googlekey = ""
    anthropickey = ""
    temperature = None
    candidate_count = None
    system_prompt = None
    google_model = None

#Google Gemini 
#model names: gemini-1.0-pro-latest gemini-1.5-pro-latest gemini-1.5-flash-latest

def init_gemini():
    #google gemini

    genai.configure(api_key=config.googlekey)

    generation_config = genai.GenerationConfig(candidate_count = None,
                                               temperature = None,
                                              )

    config.google_model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',    # gemini-1.0-pro-latest gemini-1.5-pro-latest gemini-1.5-flash-latest
                                                generation_config = generation_config
                                               )


def gemini(prompt):
    response = config.google_model.generate_content(prompt)
    return response.text


#we use ollama to address llama3:70b 
def ollama3():
    llm = Ollama(model = "llama3:70b",
                temperature = config.temperature,
                system = config.system_prompt)

    prompt = PromptTemplate(
        input_variables=["question"],
        template="Answer the following question truthfully and concice. {question}",
    )
    return LLMChain(llm=llm, prompt=prompt)


#let us also use the new gpt4o model
def gpt4():
    llm = ChatOpenAI(
        model_name = 'gpt-4o',
        api_key = config.openaikey,
        temperature=config.temperature,
        
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", config.system_prompt),
        ("human", "{question}"),
    ])
    return LLMChain(llm=llm, prompt=prompt)
    

def opus():
    llm = ChatAnthropic(model='claude-3-opus-20240229',
                        api_key=config.anthropickey,
                        temperature=config.temperature,
                        )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", config.system_prompt),
        ("human", "{question}"),
    ])
    return LLMChain(llm=llm, prompt=prompt)
    

def settings(system_prompt, temperature, candidate_count=1):
    config.system_prompt = system_prompt
    config.temperature = temperature
    config.candidate_count = candidate_count #not used atm


def printmd(string):
    display(Markdown(string))

###############
config = Configuration()

os.environ['OPENAI_API_KEY'] = ''
try:
    with open('key_openai.txt') as filein:
        config.openaikey = filein.read()
    os.environ['OPENAI_API_KEY'] = config.openaikey
except FileNotFoundError:
    print('No OpenAI key found')
    

os.environ['GOOGLE_API_KEY'] = ''
try:
    with open('key_google.txt') as filein:
        config.googlekey = filein.read()
    os.environ['GOOGLE_API_KEY'] = config.googlekey
except FileNotFoundError:
    print('No Google key found')

os.environ['ANTHROPIC_API_KEY'] = ''
try:    
    with open('key_anthropic.txt') as filein:
        config.anthropickey = filein.read()
    os.environ['ANTHROPIC_API_KEY'] = config.anthropickey
except FileNotFoundError:
    print('No Anthropic key found.')

os.environ['GROQ_API_KEY'] = ''
try:    
    with open('key_anthropic.txt') as filein:
        config.anthropickey = filein.read()
    os.environ['ANTHROPIC_API_KEY'] = config.anthropickey
except FileNotFoundError:
    print('No Groq key found.')


