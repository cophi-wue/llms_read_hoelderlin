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
import definitions as d
import os
from utils import gemini, ollama3, gpt4

%load_ext jupyter_ai_magics
```

```python

model =  ollama3("llama3", 0.8)
%ai register llama3big model

model =  gpt4()
%ai register gpt4o model

%ai register opus anthropic-chat:claude-3-opus-20240229 
```


# Reim




## Hälfte des Lebens


Correct answer: 
There are no rhymes in 'Hälfte des Lebens' only many assonances and consonances. 

```python
prompt = f"""Analyze the end rhymes in this poem: \n {d.poem_1.text}. 

Does the poem use end rhymes for all or most of its verses? 
If yes, what type of rhyme scheme does the poem use? 
If the poem uses end rhymes, list the rhyming words for each rhyme."""

print(prompt)

```

```python
%%ai llama3big
{prompt}
```

```python
%%ai gpt4o
{prompt}

```

```python
%%ai gpt4
{prompt}
```

```python
%%ai gpt4o 
{prompt}
```

```python
gemini(prompt)
```

```python
%%ai opus
{prompt}
```

## Unsere Toten

```python
prompt = f"""Analyze the end rhymes in this poem: \n {d.poem_2.text}. 

What type of rhyme scheme does the poem use? 
List the rhyming words for each rhyme."""

print(prompt)

```

Correct answer: 
The poem has a parallel rhyme schema (AABB). So the words 'Süd' and 'müd' are rhymes, 'zerfetzt' and 'gesetzt' etc.  

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
Analyze the rhymes in this poem {d.poem_2.text}. 
What type of rhyme scheme does the poem use? 
List the rhyming words for each rhyme.


```

```python
%%ai gpt4o
{prompt}
```

```python
%%ai opus
{prompt}
```

```python
gemini(prompt)
```
