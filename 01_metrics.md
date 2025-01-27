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
from utils import settings, gemini, gpt4, opus, init_gemini, printmd
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

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model 
```

# Metrics


## Hälfte des Lebens


### Level 1: General Knowledge


On this level we just ask about the metrical structure of the poem.

Solution(s): 
Each stanza has seven lines, of which three lines have three stresses and four have two.
First stanza: Of the lines with three stresses in the first stanza, a pair is placed at the beginning, and a single one at the end: The longer lines with three stresses frame the shorter ones. (Strauss assumes that the line "Es Winter ist, die Blumen, und wo" has three consecutive unstressed syllables, namely "ter ist, die".)

Second stanza also begins with two three-stressed lines. The third three-stressed line is the penultimate one.
In short:

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

#### GPT4o

```python
%%ai gpt4o
{prompt}
```

#### Anthropic Claude 3.5 Sonnet

```python
%%ai opus
{prompt}
```

#### Gemini 1.5

```python
printmd(gemini(prompt))
```

#### Evaluation and Discussion

The task  actually demands two steps: first detect the scansion, second report it in a summary way. Some of models have some difficulties to detect the correct scansion: Sonnet get's it right most of the time, while GPT-4o and Gemini 1.5 make some mistakes. 
If we just evaluate on the number of stressed syllables (looking at the patterns, not the summaries), this is the error count (using a very strict error concept where every missing or added stress is counted as one error):<br/>

GPT 4o: 7<br/>
Sonnet: 0<br/>
Gemini: 5<br/>

<br/>
Even more interesting: It is immediately obvious, that most of the LLMs are not very good in reporting their own results, that is their summaries deviate from the stress patterns they report. In their summaries they repeatedly report *more* stressed syllables than they detected. Interestingly they never report less. This is even true for Sonnet, which got the stress patterns right. We speculate that the models have no difficulty to produce any sequence of symbols, but they may have problems with remembering symbols which are not tokens. 


### level 2: Expert Knowledge

```python
prompt = f"""In some poems, a metrical device is used to indicate an important semantic aspect of the poem.  
Here is an example of this kind of interaction between metrics and semantics:

Der Tag ist grau,
das Licht so schwer,
und sie. Sie fehlt.
schuldig bin ich

The first three lines have two iambuses per line, but the last line begins with an accent that makes it a trochee, breaking the pattern. 
The word that does this is "schuldig," and the change in metre emphasizes the importance of the speaker's guilt to the poem. 

Can you find a similar use of metre in the following poem?

{poem_1.text}

"""

print(prompt)
```

#### GPT4o

```python
%%ai gpt4o
{prompt}
```

#### Claude Sonnet

```python
%%ai opus
{prompt}
```

#### Gemini

```python
printmd(gemini(prompt))
```

### level 3: Abstraction and Transfer

```python
prompt = f"""In some poems, a metrical device is used to indicate an important semantic aspect of the poem.  
Here is an example of this kind of interaction between metrics and semantics:

Der Tag ist grau,
das Licht so schwer,
und sie. Sie fehlt.
schuldig bin ich

The first three lines have two iambuses per line, but the last line begins with an accent that makes it a trochee, breaking the pattern. 
The word that does this is "schuldig," and the change in metre emphasizes the importance of the speaker's guilt to the poem. 

Can you find a similar use of metre in the following poem?

{poem_1.text}

"""

print(prompt)
```

```python

```

## Unsere Toten


### level 1: General Knowledge

The metrical structure of this poem is either quite challening to describe or ver simple, because it shows so many variations, but the variations can be explained by the underlying rule. The reason for this is: the poem uses free knittelverses. They have four stressed syllables but allow upbeats and free fillings. Vers 11 and 12 change their structure most prominently because they switch from the pattern unstressed syllable + a stressed syllabe at the end which is used throughout the poem to stressed + unstressed, a change which is emphasized by the fact that these are also rhyme words. 


```
1) -/--/--/-/
2) /--/---/-/
3) /--/-/--/
4) /--/--/--/
5) /--/--/-/
6) /-/-/--/
7) -/-/--/-/
8) /--/--/--/
9) /-/--/--/
10) /--/--/--/
11) /-/-/-/-
12) -/-/-/--/-
```

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

#### GPT4o

```python
%%ai gpt4o
{prompt}
```

#### Claude Sonnet

```python
%%ai opus
{prompt}
```

#### Gemini 1.5

```python
printmd(gemini(prompt))
```

### Level 2: Expert Knowledge

```python
prompt = f"""In some poems, a metrical device is used to indicate an important semantic aspect of the poem.  
Here is an example of this kind of interaction between metrics and semantics:

Der Tag ist grau,
das Licht so schwer,
und sie. Sie fehlt.
schuldig bin ich

The first three lines have two iambuses per line, but the last line begins with an accent that makes it a trochee, breaking the pattern. 
The word that does this is "schuldig," and the change in metre emphasizes the importance of the speaker's guilt to the poem. 

Can you find a similar use of metre in the following poem?

{poem_2.text}

"""

print(prompt)
```

#### GPT-4o

```python
%%ai gpt4o
{prompt}
```

#### Gemini

```python
printmd(gemini(prompt))
```

#### Claude Sonnet

```python
%%ai opus
{prompt}
```

#### another question
The  Knittelvers is a German vers structure which may be harder to detect, because it only counts the stressed syllables and ignores the unstressed syllables. In other words, the Knittelvers is defined by its free filling of unstressed syllables (variable number of syllables). 

```python
prompt = f"""This poem follows a  German verse meter. Which one?

{poem_2.text}"""

print(prompt)
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
printmd(gemini(prompt))
```

```python
# a veriation of the last question.
prompt = f"""The following poem follows a verse meter. Which one?

{poem_2.text}"""

print(prompt)
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
printmd(gemini(prompt))
```

### Level 3: Abstraction and Transfer


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
