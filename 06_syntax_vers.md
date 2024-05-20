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


# Syntax and Verse Structure


## Hälfte des Lebens


Expected answer: 

Syntax
In der ersten Strophe harmonischer Satzbau: eine harmonisch gebaute Periode aus zwei koordinierten, parallelen, gleich langen Satzhälften, mit der Anrede in der Mitte und durch das folgende »und« verbunden.
In der zweiten Strophe disharmonischer Satzbau: zwei unverbundene, antithetische, ungleich lange Teile: der erste Satz umfasst vier Zeilen, dann zwei kurze Sätze in den  letzten drei Zeilen, die ohne Verbindung aneinander gereiht sind. 

Syntax und Versstruktur
In der ersten Strophe decken sich immer Versende und Endes des Satzes bzw. Teilsatzes. In der zweiten Strophe dagegen haben wir eine Fülle von Enjambements. 


```python
prompt = f"""Analyze in the following poem, how the sentence structure and the vers structure relate to each other. 
In your answer, describe first the sentence structure, secondly the vers structure and then their relationsship. 
Answer this question for each stanza separately. 
In a final section interprete the relationsip between the two stanzas under this perspective. 
Here is the poem: \n {d.poem_1.text}. \n
"""

```

```python
%%ai llama3
{prompt}
```

```python
%%ai llama3big
{prompt}
```

```python
%%ai chatgpt
{prompt}
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
