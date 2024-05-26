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
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---


# Configuration

```python
from definitions import poem_1, poem_2
import os
from utils import settings, gemini, ollama3, gpt4, opus, init_gemini

%load_ext jupyter_ai_magics
```

```python
#settings
temperature = 0.8
system_prompt = "You are an expert in German literature and you are addressing other experts in German literature. You answer the questions truthfully and short."

settings(system_prompt, temperature)

```

```python
#defining aliases
init_gemini()

model =  ollama3()
%ai register llama3big model

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model 
```


# Bedeutung von (Teil-)Sätzen



Here we elicit interpretations of sentences  or parts of sentences. We concentrate on those sentences, which have a non-obvious meaning. 'meaning' doesn't refer here to an interpretation, but just to the question, what is the state o fthe fictional word described by the text.


## Hälfte des Lebens

```python
prompt = f"""We want to understand the following poem: 

{poem_1.text}

What are possible meanings of the phrase 'Das Land hänget in den See'? Describe in each case exactly what kind of landscape this phrase renders.
"""

print(prompt)
```

Expected answer:

at least three interpretations have been discussed:
* parts of the trees and bushes are extending  over the water
* there is a small peninsula (the image is basically the view from above)
* the land with its pear tree and roses is mirrored by the water


### Llama3:70b

```python
%%ai llama3big
{prompt}
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Opus

```python
%%ai opus
{prompt}
```

### Gemini 1.5

```python
gemini(prompt)
```

## Unsere Toten
