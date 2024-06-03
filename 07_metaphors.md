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
%ai register llama3 model

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model 
```


# Metaphern und andere Formen der uneigentlichen Rede.


We use a very traditional but wide definition of 'metaphor' as a figure of speech, a set of forms of non-literal speech. Here we are not interested in the differences between metaphor, metonymy, synekdoche, symbol etc. but we use the term ‘metaphor’ as a comprehensive term that encompasses these expressions. 


```python
metaphor = """In the following we define metaphor as a figure of speech, as a term which includes all forms of non-literal speech in which a verbum proprium is substituted with another term. So it includes phenomena which are sometimes also labeled as symbol, synekdoche, metonymy etc."""
```

## Hälfte des Lebens

```python
prompt = f"""Which entities or acts in the following poem can be understood as metaphors using the following definition of metaphor: {metaphor}.
For each metaphor list your reasons, why you think this is a metaphor, give your interpretation what it stands for and your reasons for this interpretation.

Here is the poem: 
{poem_1.text}
"""
print(f"{prompt}")
```

### Llama3:70b

```python
%%ai llama3
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
print(gemini(prompt))
```

## Unsere Toten

```python
prompt = f"""Which entities or acts in the following poem can be understood as metaphors using the following definition of metaphor: {metaphor}.
For each metaphor list your reasons, why you think this is a metaphor, give your interpretation what it stands for and your reasons for this interpretation.

Here is the poem: 
{poem_2.text}
"""
print(f"{prompt}")
```

### Llama3:70b

```python

```

```python
%%ai llama3
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

```python
print(gemini(f"{prompt}"))
```

```python

```
