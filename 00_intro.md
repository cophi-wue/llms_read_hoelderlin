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

<!-- #region -->
# Introduction 

This notebook contains experiments for the paper `ChatGPT reads Hölderlin. How large language models 'understand' literature.` 
the selection of our models is based on a comparison of recent models published by Openai: https://openai.com/index/hello-gpt-4o/:

<img src="model_comparison.png" alt="Model Comparison (by Openai)" width="600"/>


List of LLMs used: 

* Llama-3:70B    ✅
* ChatGPT-4o     ✅   or should we use ChatGPT 4.0 
* Gemini 1.5     ✅
* Claude Opus    ✅

<!-- #endregion -->

# Two texts

* How well do the models know Hölderlin's text?
* Does it matter, whether a model knows a text or not? Is the information used when producing new text about the reference text?
* How well does the recognition of the text type work?
* How relevant is the information about the text type?


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
%ai register llama3 model

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model 
```

# Text type 'poem'


Task: Do the models recognize the text and the text type?


## Hälfte des Lebens

```python
t1 = """
Mit gelben Birnen hänget und voll mit wilden Rosen das Land 
in den See, ihr holden Schwäne, und trunken von Küssen 
tunkt ihr das Haupt ins heilignüchterne Wasser.  
Weh mir, wo nehm’ ich, wenn es Winter ist, die 
Blumen, und wo den Sonnenschein, und Schatten der Erde? Die 
Mauern stehn sprachlos und kalt, im Winde klirren die Fahnen.
"""
```

```python
prompt = f"""I found this text in an old folder with stuff from my family. 
What kind of news text is it? Here is the text: {t1}"""
```

```python
%%ai llama3
{prompt}
```

```python
%%ai opus
{prompt}
```

```python
%%ai gpt4o
{prompt}
```

```python
print(gemini(prompt))
```

## Unsere Toten

```python
t2 = """
Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern 
wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos 
tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden 
Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage 
schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!
"""
```

```python
prompt = f"""
I found this text in an old folder with stuff from my family. 
What kind of news text is it? Here is the text: {t2}
"""
```

```python
%%ai llama3
{prompt}
```

```python
%%ai opus
{prompt}
```

```python
%%ai gpt4o
{prompt}
```

```python
print(gemini(prompt))
```

```python

```
