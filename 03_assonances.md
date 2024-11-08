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


# Assonanzen 

```python
assonance = """Assonance is a similarity in sound between two stressed syllables 
that are close together in a text, created by the same vowels but different consonants. """

assonance02 = """Assonance is the repetition of identical or similar phonemes in words or syllables that occur close together
in terms of their vowel phonemes (e.g. lean green meat)"""
```

## Hälfte des Lebens

```python
prompt = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt02 = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt_en = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""


prompt02_en = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""


prompts = [prompt, prompt02, prompt_en, prompt02_en]
```

```python
print(prompt)
```

```python

```

```python
%%ai chatgpt
for prompt in pompts:
    {prompt}
```

```python
%%ai gpt4o
for prompt in prompts:
    {prompt}
```

```python
%%ai opus
for prompt in prompts:
    {prompt}
```

```python
for prompt in prompts:
    printmd(gemini(prompt))
```

## Unsere Toten

```python
prompt = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

```

```python
%%ai gpt4o
#{prompt}
```

```python
%%ai opus
#{prompt}
```

```python
printmd(gemini(prompt))
```

```python
prompt = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt_02 = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt_en = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""


prompt02_en = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""


prompts = [prompt, prompt02, prompt_en, prompt02_en]
```

```python
%%ai chatgpt
for prompt in pompts:
    {prompt}
```

```python
%%ai gpt4o
for prompt in prompts:
    {prompt}
```

```python
%%ai opus
for prompt in prompts:
    {prompt}
```

```python
for prompt in prompts:
    printmd(gemini(prompt))
```

```python

```
