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
from utils import settings, gemini, ollama3, gpt4, opus, init_gemini

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


# Die Gedichttitel

```python

```

## Hälfte des Lebens

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

## Unsere Toten

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
