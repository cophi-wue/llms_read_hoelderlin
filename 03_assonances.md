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


# Assonanzen 

```python
assonance = """Assonance is a similarity in sound between two stressed syllables 
that are close together in a text, created by the same vowels but different consonants. """
```

## Hälfte des Lebens

```python
prompt = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {d.poem_1.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

```

```python
print(prompt)
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

## Unsere Toten

```python
prompt = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {d.poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

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
