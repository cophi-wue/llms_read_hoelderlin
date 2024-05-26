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

  # Metrics


# Configuration

```python
import os

from definitions import poem_1, poem_2
from utils import settings, gemini, ollama3, gpt4, opus, init_gemini
import utils

%load_ext jupyter_ai_magics
```

```python
#settings
temperature = 0.8
system_prompt = "You are an expert in German literature. You answer the questions truthfully and short."

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

# Metrik


Aufgabe: Analysierem welche Silben betont sind und welche unbetont.


## Hälfte des Lebens


Lösung: 
Jede Strophe hat sieben Zeilen, davon drei dreihebige und vier zweihebige.
Erste Strophe: Von den dreihebigen Versen ist in der ersten Strophe ein Paar an den Anfang gesetzt, ein einzelner an den Schluß: Die längeren dreihebigen Verse umrahmen die kürzeren. (Strauss nimmt dafür an, dass der Vers “Es Winter ist, die Blumen, und wo” drei Senkungen hintereinander hat, nämlich “ter ist, die”.)
Zweite Strophe beginnt ebenfalls mit zwei dreihebigen Versen. Der dritte dreihebige Vers ist der vorletzte. 
1. Str: 3-3-2-2-2-2-3
2. Str: 3-3-2-2-2-3-2

```python
prompt = f"""Analyze the scansion of the following poem, i.e. describe which syllables are stressed and which are not. 
Give the answer using the following characters to indicate stressed syllables and not stressed syllables: / for a stressed syllable and - for an unstressed syllable. 
Number the lines of the poem and use these numbers at the beginning of each line of output. At the end add  for each stanza  the numbers of stressed syllables per vers. 
Example: For the two lines “The house is green / the mouse is dead.” the output would look like this:
1: -/-/
2: -/-/
stressed syllables: 2-2

Here is the poem: 
{poem_1.text}
"""
print(prompt)
```

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
print(gemini(prompt))

```

### Evaluation and Discussion

The task  actually demands two steps: first detect the scansion, second report it in a summary way. All of the models are far from being perfect in detecting the correct scansion. 
If we just evaluate on the number of stressed syllables (looking at the patterns, not the summaries), this is the error count:<br/>
Llama3: 6<br/>
GPTo: 5<br/>
Opus: 4<br/>
Gemini: 20(!)<br/>

<br/>
Maybe even more interesting: It is immediately obvious, that most of the LLMs are not very good in reporting their own results. With the exception of Opus all report in their summaries repeatedly *more* stressed syllables than they detected. Interestingly they never report less.


## Unsere Toten

```python
prompt = f"""Analyze the scansion of the following poem, i.e. describe which syllables are stressed and which are not. 
Give the answer using the following characters to indicate stressed syllables and not stressed syllables: / for a stressed syllable and - for an unstressed syllable. 
Number the lines of the poem and use these numbers at the beginning of each line of output. At the end add  for each stanza  the numbers of stressed syllables per vers. 
Example: For the two lines “The house is green / the mouse is dead.” the output would look like this:
1: -/-/
2: -/-/
stressed syllables: 2-2

Here is the poem: 
{poem_2.text}
"""
print(prompt)
```

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

```python

```
