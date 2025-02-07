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
from utils import settings, gemini, gpt4, opus, init_gemini, printmd
import utils

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


# Rhyme




## Hälfte des Lebens


### Level 1: General Knowledge


We are just asking for the detection of rhymes in the poem. 
First we want to know whether there are any (end) rhymes. If yes, which words are rhymed and finally what kind of rhyme schema there is, like ABAB or AABB or ABBA etc.

Correct answer: 
There are no rhymes in 'Hälfte des Lebens' only many assonances and consonances. 

```python
prompt = f"""Analyze the (end) rhymes in this poem: \n {poem_1.text}. 

Does the poem use rhymes for all or most of its verses? 
If yes, what words are rhymed and what type of rhyme scheme does the poem use (like AABB or ABAB or ABBA etc.)? 
"""

print(prompt)

```

#### GPT-4o

```python
%%ai gpt4
{prompt}
```

#### Gemini 1.5

```python
printmd(gemini(prompt))
```

#### Claude Sonnet

```python
%%ai opus
{prompt}
```

### Level 2: Expert Knowledge


As there is no rhyme in HdL, there is no meaningful expert question to be asked (False answer would probably mostly be false because the falsely detect rhymes).




### Level 3: Abstraction and Transfer


As rhyme is just a special case of assonances, see the complex probing experiments there.


## Unsere Toten


### Level 1: General Knowledge

We are just asking for the detection of rhymes in the poem. 

Correct answer: 


```python
prompt = f"""Analyze the (end) rhymes in this poem: \n {poem_2.text}. 

Does the poem use rhymes for all or most of its verses? 
If yes, what words are rhymed and what type of rhyme scheme does the poem use (like AABB or ABAB or ABBA etc.)? 
"""

print(prompt)

```

Correct answer: 
The poem has a parallel rhyme schema (AABB). So the words 'Süd' and 'müd' are rhymes, 'zerfetzt' and 'gesetzt' etc.  


#### Gpt-4o

```python
%%ai gpt4
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


Can we detect an additional semantic structure, an additional layer of meaning, if we just look at the rhyme words of the poem? What would be plausible interpretative strategies and do they work (i.e. are they productive, do they produce any additional insights) for this poem?

Expected answer: Two possible directions of analysis could be expected: 
1) one follows the meaning which is etablished by pairing words in a rhyme. There is not a lot of this happening in the first half, but in the second half, we see that 'wacht' and 'Nacht' belong somewhat to opposites, similarly 'schwer' (which recalls the 'müd' (tired)) and 'Begehr'. Finally the last rhyme 'zerfressen' (eaten away) and vergessen (forgotten) implies an even stronger semantic relation, but not of opposites, rather both imply that there has been something which is no getting lost in a painful process. 
2) The second looks at the vowels of the rhymes and connects them to the tone and mood of the poem. We cannot detect anything which would be the basis for an interesting and productive description. 

```python
prompt = f"""Describe at least two strategies to analyze the rhyme structure of poems in relation to the meaning of the poem or parts of the poem. 
Then analyze whether they produce interesting insights when applied to the following poem:

{poem_2.text}. 

"""

print(prompt)

```

```python
%%ai gpt4o
{prompt}
```

```python
printmd(gemini(prompt))
```

```python
%%ai opus
{prompt}
```

```python

```

### Level 3: Abstraction and Transfer


As rhyme is just a special case of assonances, see the complex probing experiments there.

```python

```
