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


# Metaphors and other forms of figurative speech.


We are interested in local figures of speech like metaphors, metonymies, synekdoches, symbols. 'Local' because their scope is usually just one entity or one type of entity, not the whole text. 





```python
figurative_speech = """All forms of non-literal speech in which a verbum proprium (what the thing is really called) is substituted with another term. 
So it includes phenomena which are sometimes also labeled as metaphor, synekdoche, metonymy,  symbols etc. """
```

## Hälfte des Lebens


### Level 1: General knowledge
We ask directly for forms of figurative speech. 

There is no real ground here and the interpretations of the poem have different descriptions of this aspect. 
All agree that the 'Schwäne' are a symbol, and most agree that the landscape and its element in the first stanza and the artefacts in the second stanza are symbols, that is they cannot translated into a 'literal' meaning but are signs in a broader sense.

One aspect which has been debated is the phrase "hänget / [...] / Das Land in den See," What does it mean on the literal level (hard to understand: does it describe a peninsula - seen from above - or how the twigs full of fruits touch the water) and what is its symbolic meaning (easier to understand). 


```python
prompt = f"""Which entities or acts in the following poem can be understood as figurative speech using the following definition : {figurative_speech}.
For each instance of figurative_speech list your reasons, why you think this is one, give your interpretation what it stands for and your reasons for this interpretation.

Here is the poem: 
{poem_1.text}

List all of them.
"""
print(f"{prompt}")
```

#### GPT4o

```python
%%ai gpt4o
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


We want to discuss how the meaning of figurative language in the poem changes, when we add some historical information. In the case of Hälfte des Lebens, we add the information, that Hölderlin was a great admirer of antiquity and its literature and that in the old greek and latin literature the swan was often a metaphor for the poet.

```python
prompt = f"""The German poet Friedrich Hölderlin wrote the following poem around 1800: 

{poem_1.text}

Interpret the meaning of the swans in the context of the poem.

How does this interpretation change, when we know that Hölderlin was a great admirer of antiquity? 
He looked up to its literature as a model for his own writing. In antiquity, the swan is often 
regarded as a symbol for the poet. 
How does this knowledge change the interpretation of the swans and the poem?
"""

print(prompt)
```

#### GPT-4o

```python
%%ai gpt4o
{prompt}
```

#### Gemini 1.5

```python
print(gemini(prompt))
```

#### Sonnet 3.5

```python
%%ai opus
{prompt}
```

## Unsere Toten

```python

```

```python
prompt = f"""Which entities or acts in the following poem can be understood as figurative speech using the following definition : {figurative_speech}.
For each instance of figurative_speech list your reasons, why you think this is one, give your interpretation what it stands for and your reasons for this interpretation.

Here is the poem: 
{poem_2.text}

List all of them.
"""
print(f"{prompt}")
```

#### GPT4-o

```python
%%ai gpt4o
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

```python
prompt = f"""Interpret the meaning of 'Germany' in the following poem which bears the title 'Unsere Toten': 

{poem_2.text}

The first and only publication of the poem was in the book "Die deutsche Balladen-Chronik. Ein Balladenbuch von deutscher Geschichte und deutscher Art. Dortmund: Ruhfus 1922"  How does this information 
change your understanding of the word 'Germany' and its meaning in the context of the poem?

"""

print(prompt)
```

#### Gpt4o

```python
%%ai gpt4o
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

# Experiment 2

How does the addition of specific knowledge - what the swans stood for in antiquity and that Hölderlin had profound knowledge of the antiquity and that classic literature provided the model for his literature - change the interpretation? 

```python

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
