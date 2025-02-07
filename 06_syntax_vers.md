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
from utils import settings, gemini, gpt4, opus, init_gemini, printmd

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


# Syntax and Verse Structure


## Poem 1: Hälfte des Lebens


### Level 1: General Knowledge


On this level, we ask for a comparison of the general syntacic structure in the stanzas.

Solution: 

In the first stanza, harmonious sentence structure: a harmoniously constructed sequence of two coordinated, parallel, equally long sentence halves, with a form of address in the middle and connected by the following “und”.
In the second stanza, disharmonious sentence structure: two unconnected, antithetical parts of unequal length: the first sentence comprises four lines, then two short sentences in the last three lines, which are strung together without a connection. 


```python
prompt = f"""Analyze the syntax of the following poem by comparing the sentence structures in its two stanzas. 
First analyze each stanza individually and then compare the results for both stanzas.

Here is the poem: 
{poem_1.text}
"""
print(prompt)
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet

```python
%%ai opus
{prompt}
```

### Gemini

```python
printmd(gemini(prompt))
```

## Level 2: Expert Knowledge


On this level, we ask for the relation of syntax and verse structure.

Solution:
In the first stanza, the end of the verse and the end of the sentence or clause always coincide. 
This is not the case in the second stanza: Phrase structure and verse structure are often not aligned, there are many enjambments. 

[Task 2b: Ask for anastrophes]


```python
prompt = f"""Analyze in the following poem how the sentence structure and the vers structure relate to each other. Consider sentence and clause structure.
Answer this question for each stanza separately. 
In a final section interprete the relationsip between the two stanzas under this perspective. 

Here is the poem:  
{poem_1.text}. 
"""
print(prompt)
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
printmd(gemini(prompt))
```

## Level 3: Transfer and Abstraction


Skipped for this pheonomenon

```python
prompt = f"""Analyze in the following poem, 

Here is the poem: \n {poem_1.text}. \n
"""
print(prompt)
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
printmd(gemini(prompt))
```

# Poem 2: Unsere Toten


## Level 1: General Knowledge

```python
prompt = f"""Analyze the syntax of the following poem. Consider sentence and clause structure.

Here is the poem: 
{poem_2.text}
"""
print(prompt)
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet

```python
%%ai opus
{prompt}
```

### Gemini

```python
printmd(gemini(prompt))
```

# Level 2: Expert Knowledge

```python
prompt = f"""Analyze in the following poem how the sentence structure and the vers structure relate to each other. 
Take sentence and clause structure into account.

Here is the poem:  
{poem_2.text}. 
"""
print(prompt)
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet

```python
%%ai opus
{prompt}
```

### Gemini

```python
printmd(gemini(prompt))
```

# Level 3: Transfer and Abstraction


Skipped for this phenomenon.
