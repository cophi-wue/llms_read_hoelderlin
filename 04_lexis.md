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


# Lexis


## Poem 1: Hälfte des Lebens


### Level 1: General Knowledge


On the student level we ask about semantic fields in the vocabulary. Analyzing each stanza individually.
We also ask whether the distribution of parts of speech in the poem relates to the semantic fields of the stanzas. 

Solution(s): 
Stanza 1: Summer, nature, animate, interaction; 
Stanza 2: Winter, coldness, inanimate objects, isolation

Parts of speech (PoS): There is an asymmetry in distribution: attribute adjectives that are modifying nouns only occur in the first stanza, in the secon stanza the nouns are bare which relates to the semantic fields of coldness, isolation


```python
prompt = f"""Analyze the lexis of the following poem by describing for each stanza which semantic fields are particularly prominent in the vocabulary of the individual stanzas. 
Do particular parts of speech relate to the semantic fields?

Here is the poem: 
{poem_1.text}
"""
print(prompt)
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet (Opus)

```python
%%ai opus
{prompt}
```

### Gemini 1.5

```python
printmd(gemini(prompt))
```

### Conclusion

All three models describe meaningful semantic fields and provide them with correct example words. The part of speech recognition is also mostly correct. While Gpt4o only gives examples of lexical parts of speech, Sonnet mentions the interjection "weh" and refers somewhat cryptical to "interrogative construction" instead of parts of speech. 

Gemini is relatively verbose and makes some faulty claims: The polysemous verb "hängen", which is used as intransitive verb describing a state in the poem, is incorrectly identified as (transitive) verb of action. The subordinating conjuntion "wenn" is incorrectly classified as interrogative pronoun.

Sonnet identifies a "Sacred/transcendent field" based on adjectives "heilignüchtern" and  "hold" that stand out because they are not part of everyday language.

Interestingly, the models always name 3 semantic fields for each stanza, although this was not specified in the prompt. The only exception is Sonnet by listing 4 semantic fields for the second stanza.

Sonnet answers somewhat taciturnly and doesn't quite follow the analysis sequence laid out in the prompt.

The prompt does not ask for the poem's author and title, yet Gpt4o and Gemini both generate this information. While GPTo4 does this correctly, 
Gemini incorrectly attributes the poem to Rilke. For GPTo4 this could mean that the poem itself and possibly some interpretations were seen in the training data.


### Task 1b: final

```python
prompt = f"""Analyze the lexis of the following poem:
(i) by describing for each stanza which semantic fields are particularly prominent in its vocabulary; 
(ii) by evaluating the distribution of parts of speech in the stanzas in relation to their semantic fields.


Here is the poem: 
{poem_1.text}
"""
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

## Level 2: Expert Knowledge


On this level we ask about contrasts that are triggered by the vocabulary either in complex words or at the phrasal level.

We expect that "heilignüchtern" is desribed as an oxymoron (trope); could be identified as pivotal point between the general meanings of the two stanzas;
The word can also be related to the poetological topos of "sobria ebrietas" meaning "sober extasy", i.e. a good spiritual state opposed to mundane extasy derived from vine and other drugs.

```python
prompt = f"""Analyze the lexis of the following poem by focusing on one semantic contrast that is triggered either by a morphologically complex word or within a phrase. 
Elaborate how this contrast contributes to the meaning of the poem.

Here is the poem: 
{poem_1.text}
"""
print(prompt)
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet

```python
%%ai opus
{prompt}
```

### Gemini 1.5

```python
printmd(gemini(prompt))
```

### Conclusion:
All three models analyze "heilignüchterne" as the most striking example of semantic contrast. Only Sonnet makes use of specialized vocabulary describing "heilignüchtern" as "oxymoronic combination". No model refers to the topos of "sobria ebriatas"


### Task 2b

```python
prompt = f"""The word "heilignüchterne" in the following poem is an interesting word. What does it mean in the context of the poem? 
Elaborate on its stylistic and poetological topoi.

Here is the poem: 
{poem_1.text}
"""
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




## Level 3: Abstraction and Transfer

<!-- #region -->
On this level ....


Solution:
The code is to interpret attributive adjectives (in contrast to predicatively used ones) in terms of their antonym or semantic opposite, 
in the first Stanza of "Hälfte des Lebens" this affects: "wilde-zahme" (wild-tame), "holden-häßlichen" (lovely/graceful-ugly/clumsy), "heilignüchtern-profanbesoffen". 
For the color adjective "gelb" (yellow) there is no semantic antonym. Instead it would be possible to use the complementary color in the color wheel 
which is purple. The new scenery that emerges is wild and alludes to a drug fantasy.
<!-- #endregion -->

```python
prompt = f"""The German poet Sori Egin developed a special semantic code in her poetic language that creates a vibrant level of semantic tension.
Here is an example and its interpretation:

Die Nacht ist dunkel, tief und klar,  
der trübe Mond leuchtet allein.    
Ein unruhiger Traum schwebt wunderbar,  
in Frieden möcht’ ich ewig sein.

The night is dark, deep and clear,  
the clear moon shines alone.    
A peaceful dream floats wonderfully,  
I would like to be at peace forever

Apply this code to the first stanza of the following poem and describe what kind of scenery emerges. 
 
Here is the poem: 
{poem_1.text}
"""
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

## Poem 2: Unsere Toten


## Level 1: General Knowledge

```python
prompt = f"""Analyze the lexis of the following poem:
(i) by describing for each stanza which semantic fields are particularly prominent in its vocabulary; 
(ii) by evaluating the distribution of parts of speech in the stanzas in relation to their semantic fields.


Here is the poem: 
{poem_2.text}
"""
print(prompt)
```

### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet

```python
%%ai opus
{prompt}
```

### Gemini 1.5

```python
printmd(gemini(prompt))
```

## Level 2: Expert Knowledge


Solution: "schmerzzerfressen" is compuond, hyperbole

```python
prompt = f"""The word "schmerzzerfressen" in the following poem is an interesting expression. What does it mean in the context of the poem? 
Elaborate on its meaning related to its form in terms of lexical stylistic features.

Here is the poem: 
{poem_2.text}
"""
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
### Conclusion
Gemini 


```

## Level 3: Abstraction and Transfer

```python
prompt = f"""The German poet Sori Egin developed a special semantic code in her poetic language that creates a vibrant level of semantic tension.
Here is an example and its interpretation:

Die Nacht ist dunkel, tief und klar,  
der trübe Mond leuchtet allein.    
Ein unruhiger Traum schwebt wunderbar,  
in Frieden möcht’ ich ewig sein.

The night is dark, deep and clear,  
the clear moon shines alone.    
A peaceful dream floats wonderfully,  
I would like to be at peace forever

Apply this code to the following poem and describe what kind of scenery emerges. 
 

Here is the poem: 
{poem_2.text}
"""
print(prompt)
```

### Gpt4o

```python
%%ai gpt4o
{prompt}
```

### Sonnet

```python
%%ai opus
{prompt}
```

### Gemini 1.5

```python
printmd(gemini(prompt))
```

### Conclusion:
AGPTo4 and Gemini apparently induce the rule correctly, Sonnet corrects the inpute as counterfactual.
