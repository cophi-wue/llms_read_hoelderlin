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
