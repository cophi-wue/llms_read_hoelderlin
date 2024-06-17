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

# Configuration

```python
from definitions import poem_1, poem_2
from utils import settings, gemini, ollama3, gpt4, opus, init_gemini
import utils

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


# Reim




## Hälfte des Lebens


Correct answer: 
There are no rhymes in 'Hälfte des Lebens' only many assonances and consonances. 

```python
prompt = f"""Analyze the end rhymes in this poem: \n {poem_1.text}. 

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
print(gemini(prompt))
```

```python
#%%ai opus
{prompt}
```

## Unsere Toten

```python
prompt = f"""Analyze the end rhymes in this poem: \n {poem_2.text}. 

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
Analyze the rhymes in this poem {poem_2.text}. 
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
print(gemini(prompt))

```

```python

```
