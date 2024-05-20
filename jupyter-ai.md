---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.2
  kernelspec:
    display_name: ds
    language: python
    name: ds
---

## Anleitung
Am Anfang einer Notebook-Zelle schreibt man '%%ai' und dann das alias des Sprachmodells, das man verwenden will. <br/>
Mit 'chatgpt' richtet man z.B. seine Anfragen an 'gpt-3.5-turbo'. Für uns besonders relevant sind z.Zt. 'chatgpt', 'gpt4' und 'llama3'. <br/>
Statt des kurzen alias kann man auch den ausführlichen Namen verwenden. <br/>
Wer alle Modelle, die jupiter-ai zur Zeit unterstützt, sehen will, kann das mit '%ai list' (Achtung, nur 1 Prozehntzeichen). <br/>
Leider wird ollama noch nicht direkt unterstützt, deshalb habe ich ein eigenes alias für llama3 gesetzt. Kann man leicht ergänzen.<br/>

Nicht vergessen, in der nächsten Zeile den OPENAI-API-Key zu setzen. Keine Anführungszeichen nach dem =-Zeichen!

```python
import os

with open('openai_key.txt') as filein:
    openaikey = filein.read()

os.environ['OPENAI_API_KEY'] = openaikey
```

```python
%load_ext jupyter_ai_magics
```

```python
#python imports
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama    

```

```python
#ollama not directly supported in jupyter-ai, so we need this custom function.
#easy to adapt to other models than llama-3
llm = Ollama(model = 'llama3',
             temperature = 0.6 )

prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question truthfully and concice. {question}",
)
chain = LLMChain(llm=llm, prompt=prompt)

%ai register llama3 chain
```

```python
%%ai llama3
```

Am Anfang einer Notebook-Zelle schreibt man '%%ai' und dann das alias des Sprachmodells, das man verwenden will. 
Mit 'chatgpt' richtet man seine Anfragen an 'gpt-3.5-turbo'. Statt des kurzen alias kann man auch den ausführlichen Namen verwenden.
Wer alle Modelle, die jupiter-ai zur Zeit unterstützt, sehen will, kann das mit '%ai list' (Achtung, nur 1 Prozehntzeichen).
Leider wird ollama noch nicht direkt unterstützt, deshalb habe ich ein eigenes alias gesetzt.

```python
%%ai chatgpt
You are a professor for German literature and a specialist for the poetry of Friedrich Hölderlin. Explain, why the poem 'Hälfte des Lebens' is so famous. 
```

```python
%%ai llama3 
You are a professor for German literature and a specialist for the poetry of Friedrich Hölderlin. Explain, why the poem 'Hälfte des Lebens' is so famous. 
```

```python
prompt = "Describe how the poem 'Hälfte des Lebens' by the German poet Friedrich Hölderlin is organized formally and support your analysis with quotes from the text (the quotes are in German)."
```

```python
%%ai chatgpt
{prompt}
```

```python
%%ai llama3 
{prompt}
```

```python
poem = """Hälfte des Lebens

Mit gelben Birnen hänget
Und voll mit wilden Rosen
Das Land in den See,
Ihr holden Schwäne,
Und trunken von Küssen
Tunkt ihr das Haupt
Ins heilignüchterne Wasser.

Weh mir, wo nehm’ ich, wenn
Es Winter ist, die Blumen, und wo
Den Sonnenschein,
Und Schatten der Erde?
Die Mauern stehn
Sprachlos und kalt, im Winde
Klirren die Fahnen. """
```

```python
formal_structure = "The concept of formal structure or formal organization of a poem refers to aspects like rhyme, meter, rhythm. How does the sentence structure align with the verses? etc." 
```

```python
prompt =f"""Analyze the formal structure of the poem 'Hälfte des Leben'. Here is the full text of the poem: {poem}. Here is a definition of the concept formal structure: {formal_structure}. Use quotes from the text in your analysis."""
```

```python
%%ai llama3
{prompt}
```

```python
%%ai chatgpt
{prompt}
```

```python
%%ai gpt4
{prompt}
```

```python

```
