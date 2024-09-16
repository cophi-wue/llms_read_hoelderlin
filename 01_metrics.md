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

  # Meter


# Configuration

```python
import os

from definitions import poem_1, poem_2
from utils import settings, gemini, ollama3, gpt4, opus, init_gemini, printmd
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

# Metrik


Aufgabe: Analysierem welche Silben betont sind und welche unbetont.

todo: 

* wie sprachspezifisch ist die Kompetenz der Modelle? Vergleich mit einem englischen Text notwendig.
* 


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
Example: For the two stanzes each with two lines 
"The house is green
The mouse is dead. 

I wonder still
Who pays my bill."

The output would look like this:
1: -/-/
2: -/-/
3: //-/
4: //-/

At the end repeat the numbers of stressed sylables for each line for each stanza like this:

Stanza 1: 2-2
Stanza 2: 3-3

Here is the poem: 
{poem_1.text}
"""
print(prompt)
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
gemini(prompt)
```

## Language bias in metrical analysis

```python
t = """
One face looks out from all his canvases,
One selfsame figure sits or walks or leans:
We found her hidden just behind those screens,
That mirror gave back all her loveliness.
A queen in opal or in ruby dress,
A nameless girl in freshest summer-greens,
A saint, an angel—every canvas means
The same one meaning, neither more or less.
He feeds upon her face by day and night,
And she with true kind eyes looks back on him,
Fair as the moon and joyful as the light:
Not wan with waiting, not with sorrow dim;
Not as she is, but was when hope shone bright;
Not as she is, but as she fills his dream.
"""
```

```python
prompt = f"""Analyze the scansion of the following poem, i.e. describe which syllables are stressed and which are not. 
Give the answer using the following characters to indicate stressed syllables and not stressed syllables: / for a stressed syllable and - for an unstressed syllable. 
Number the lines of the poem and use these numbers at the beginning of each line of output. At the end add  for each stanza  the numbers of stressed syllables per vers. 
Example: For the two stanzes each with two lines 
"The house is green
The mouse is dead. 

I wonder still
Who pays my bill."

The output would look like this:
1: -/-/
2: -/-/
3: //-/
4: //-/

At the end repeat the numbers of stressed sylables for each line for each stanza like this:

Stanza 1: 2-2
Stanza 2: 3-3

Here is the poem: 
{t}
"""

```

<!-- #raw -->
# human description



Like all sonnets, "In an Artist's Studio" uses iambic pentameter. That means that each line has five iambs, metrical feet that follow a da-DUM stress pattern. Take line 9:

    He feeds | upon | her face | by day | and night,

But like a lot of sonnets, this one often does some fancy footwork within its pentameter, moving stresses around to emphasize important moments. For instance, take a look at what happens at the end of the poem:

    Not as | she is, | but was | when hope | shone bright;
    Not as | she is, | but as | she fills | his dream.

These two closing lines start with trochees, feet that go DUM-da. That front-loaded meter makes the speaker's closing thoughts feel urgent and pointed: as she insists that these portraits show the model "Not as she is," she leans hard on the word "Not."
(Source: https://www.litcharts.com/poetry/christina-rossetti/in-an-artist-s-studio)

<!-- #endraw -->

```python
%%ai llama3
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
print(gemini({prompt}))
```

### Results
* llama3 doesn't work at all (the lines are chopped and therefore the number of stressed sylables is false)
* GPT4o falsely sees six stressed sylables in the detail analysis in vers 1, 2, 11. And it doesn't get the two trochees at the end.  
* Opus doesn't recognize the pentameter and doesn't see the trochees in the last two lines.
* Gemini doesn't see the pentameter and changes its count between 4 and 5 stresses, but it gets the trochees. 
* Btw: Gpt4o splits the poem into an octet and a sextet, which is actually true for the Petrarchan sonnet, but not for this poem, which has only one stanza. 



## Can large language models count?

```python
prompt = f"""In the following poem count the number of vowels for each word in a vers. Report the results in the following fashion: 

1: 4 2 1 3
2: 2 4 1 2 
 etc. 

At the end report the number of vowels per line for each stanza like this:

1. stanza: 10 - 9 
2. stanza: 9 - 11

If the first two stanzas look like this: 

"It happens to the best of us 
that life feels like a passing bus

and we stay here and there 
it goes and leaves."

the answer would be:

1: 1 2 1 1 1 1 1 
2: 1 2 3 2 1 2 1 

3: 1 1 1 2 1 2 
4: 1 2 1 3

1. stanza: 8 - 12
2. stanza: 8 - 7

Here is the poem: 

{poem_1.text}
"""
print(f"{prompt}")
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
print(gemini({prompt}))
```

No, they cannot.


# Results and Discussion


The metrical analysis of both poems shows across the models a surprisingly high amount of errors. The answers also show, that the models have difficulties to remember their own results. These errors are not caused by the fact that we analyze German poems, but can also be seen in a quite famous English poem. 

```python

```
