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
import os
from utils import settings, gemini, ollama3, gpt4, opus, init_gemini, printmd

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


# Metaphors and other forms of figurative speech.


We use a very traditional but wide definition of 'metaphor' as a figure of speech, a set of forms of non-literal speech. Here we are not interested in the differences between metaphor, metonymy, synekdoche, symbol etc. but we use the term ‘metaphor’ as a comprehensive term that encompasses these expressions. 


```python
metaphor = """In the following we define metaphor as a figure of speech, 
as a term which includes all forms of non-literal speech 
in which a verbum proprium (what the thing is really called) is 
substituted with another term. 
So it includes phenomena which are sometimes also labeled 
as symbol, synekdoche, metonymy etc."""
```

# Experiment 1
We ask directly for forms of figurative speech


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
printmd(gemini(prompt))
```

## Unsere Toten

```python
prompt = f"""Which entities or acts in the following poem can be understood as figurative speech 
using the following definition of figurative speech: {metaphor}.
For each occurrence of figurative speech list your reasons, why you think this is figurative speech, 
give your interpretation what it stands for and your reasons for this interpretation.

Here is the poem: 
{poem_2.text}
"""
print(f"{prompt}")
```

### Llama3:70b

```python
%%ai llama3
{prompt}
```

```python

```

# Experiment 2

How does the addition of specific knowledge - what the swans stood for in antiquity and that Hölderlin had profound knowledge of the antiquity and that classic literature provided the model for his literature - change the interpretation? 

```python
prompt = f"""The German poet Friedrich Hölderlin wrote the following poem around 1800: 

{poem_1.text}

Interpret the meaning of the swans in the context of the poem.

How does this interpretation change when we know that Hölderlin was a great admirer of antiquity? 
He looked up to its literature as a model for his own writing. In antiquity, the swan is often 
regarded as a symbol for the poet. 
How does this knowledge change the interpretation of the swans and the poem?
"""

print(prompt)
```

Expectations:

The knowledge should change the interpretation of the swan from natural entities or symbols of lovers to a symbol of the poet. This should additionally foreground two aspects: 1) communication and 2) relation. In the first stanza everything is connected with each other, while in the second stanza everything is isolated. In the second stanza this isolation is explicitly related to commnication resp. the impossibility to communicate ('sprachlos'). 


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
printmd(gemini(f"{prompt}"))
```

```python

```

# Experiment 3

```python
prompt = f"""
In the poem 'Hälfte des Lebens' by Friedrich Hölderlin literary scholars were always 
puzzled by the phrase 'im Winde | Klirren die Fahnen'. There are two competing interpretations. 
One assumes, 'Fahnen' refers to flags. The other 'Fahnen' refers to weathervanes. The German language
at that time (1800) knows both meanings of 'Fahne'. 
What is the better interpretation? Give your reasons and explain how it changes the meaning of the text. 

Here is the poem:

{poem_1.text}
"""

print(prompt)
```


Expectations:

Choice: Weathervanes.
Reason: 'klirren' better suited for metal. Cold metal fits better to the imagery of the second stanza.
Weathervanes are man made objects like the second other important entity in the stanza, the wall.


## GPT4o

```python
%%ai gpt4o
{prompt}
```

## Opus

```python
%%ai opus
{prompt}
```

## Gemini

```python
printmd(gemini(f"{prompt}"))
```

```python

```
