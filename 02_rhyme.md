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
from utils import settings, gemini, gpt4, opus, init_gemini, printmd
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

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model 
```


# Rhyme




## Hälfte des Lebens


### Level 1: General Knowledge


We are just asking for the detection of rhymes in the poem. 
First we want to know whether there are any (end) rhymes. If yes, which words are rhymed and finally what kind of rhyme schema there is, like ABAB or AABB or ABBA etc.

Correct answer: 
There are no rhymes in 'Hälfte des Lebens' only many assonances and consonances. 

```python
prompt = f"""Analyze the (end) rhymes in this poem: \n {poem_1.text}. 

Does the poem use rhymes for all or most of its verses? 
If yes, what words are rhymed and what type of rhyme scheme does the poem use (like AABB or ABAB or ABBA etc.)? 
"""

print(prompt)

```

#### GPT-4o

```python
%%ai gpt4
{prompt}
```

#### Gemini 1.5

```python
printmd(gemini(prompt))
```

#### Claude Sonnet

```python
%%ai opus
{prompt}
```

### Level 2: Expert Knowledge


### Level 3: Abstraction and Transfer


## Unsere Toten


### Level 1: General Knowledge

We are just asking for the detection of rhymes in the poem. 

Correct answer: 


```python
prompt = f"""Analyze the (end) rhymes in this poem: \n {poem_2.text}. 

Does the poem use rhymes for all or most of its verses? 
If yes, what words are rhymed and what type of rhyme scheme does the poem use (like AABB or ABAB or ABBA etc.)? 
"""

print(prompt)

```

Correct answer: 
The poem has a parallel rhyme schema (AABB). So the words 'Süd' and 'müd' are rhymes, 'zerfetzt' and 'gesetzt' etc.  


#### Gpt-4o

```python
%%ai gpt4
{prompt}

```

#### Gemini 1.5

```python
printmd(gemini(prompt))

```

#### Sonnet 

```python
%%ai opus
{prompt}
```

### Level 2: Expert Knowledge


### Level 3: Abstraction and Transfer

```python

```
