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


# Bedeutung von (Teil-)Sätzen



Here we elicit interpretations of sentences  or parts of sentences. We concentrate on those sentences, which have a non-obvious meaning. 'Meaning' doesn't refer here to an interpretation, but just to the question, what is the state of the fictional word described by the text. These experiments are related to the analysis of metaphorical expressions (cf. Notebook 07). 


## 1. Hälfte des Lebens (1804)


The basic structure of the poem is simple. The two stanzas, representing the two "halves of life," are arranged antithetically to each other. The antithetical structure is essentially supported by four phrases or parts of sentences, namely "das Land hänget in den See", "die holden Schwäne trunken“, "die Mauern stehn sprachlos" und "im Winde klirren die Fahnen". The summer stanza portrays a harmonious landscape where everything is interconnected and alive, while the winter stanza depicts a scene of separation, silence, and lifelessness (Schmidt).


**"Das Land hänget im See"** 


Using the phrase "Das Land hänget im See" as an example, this study aims to compare the techniques of zero-shot prompting and few-shot prompting. Zero-shot prompting refers to using a prompt to interact with the model without providing any examples or demonstrations. The zero-shot prompt directly instructs the model to perform a task without additional examples to guide it. Conversely, few-shot prompting can be employed as a technique to enable in-context learning.

This experiment seeks to explore the insight provided by Liu et al.: "LMs do not make use of the metaphorical context well, instead relying on the predicted probability of interpretations alone [...]" (2022, p. 4438).

```python
prompt = f"""We want to understand the following poem: 

{poem_1.text}

What are possible meanings of the phrase 'Das Land hänget in den See'? Describe in each case exactly what kind of landscape this phrase renders.
"""

print(prompt)
```

Expected answer:

at least three interpretations have been discussed:
* parts of the trees and bushes are extending  over the water
* there is a small peninsula (the image is basically the view from above)
* the land with its pear tree and roses is mirrored by the water


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

**"Ihr holden Schwäne trunken von Küssen tunkt ihr das Haupt"**


Using the phrase "Ihr holden Schwäne, und trunken von Küssen tunkt ihr das Haupt," a comparative analysis will be conducted to examine how the structure or an inverted sentence order affects the models' non-literal reasoning. In the poem, "Ihr holden Schwäne" is an invocation directed at the poet. The image of the swans serves as a metaphor for the poetic existence.

How does the interpretation of the phrase change through the reordering of its components? The reordered sentences are: "Trunken von Küssen tunkt ihr holden Schwäne das Haupt" or "Das Haupt tunkt ihr holden Schwäne trunken von Küssen"

Of particular interests: 
- Studying  how the syntactic structure influences the models' understanding and interpretation of non-literal language.
- This analysis explores the models' sensitivity to syntactic variations and their impact on the comprehension of metaphorical contexts.

Prompt design: 
- Guided Chain of Tasks
- Chain-of-Thought
- Time sequences

```python
prompt = f"""What are the possible meanings of two phrase 1,2,3? 

phrase 1: Ihr holden Schwäne, und trunken von Küssen, tunkt ihr das Haupt
phrase 2: Das Haupt tunkt ihr holden Schwäne trunken von Küssen"
phrase 3: Trunken von Küssen tunkt ihr holden Schwäne das Haupt

Do the following step by step:
1. Analyze the phrases synatically and provide a part-of-speech-tagging for each phrase. 
2. After that: What are the most possible meaning for each phrases?
"""

print (prompt)
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

**"Die Mauern stehn sprachlos"**


Using the example sentence 'The walls stand speechless and cold,' we investigate how different models complete clauses with the suffix 'that is to say.' The completion function might also be measured with various temperatures: 0.2, 0.4, 0.8, and 1.

In the first step, the models generate a completion of the sentence without the context of the poem 'Half of Life.' In the second step, the models should choose which completion fits best in the context of the poem. The individual clauses should then be ranked.

Of particular interest for us: 
By analyzing completions generated by different models, we might gain a comprehensive understanding of each model's creativity, coherence and contextual understanding.
Do the models each select their "own" completion?

Prompt design:
- Generate completions (without refering to the poem), experiments with different temperatures
- Each model chooses the "best" completions for the context of the poem
- (Rank each completions)
  
Expected answers (Schmidt): 
- Within the speechless walls, the nature remains silent towards the lyrical I, which was once entirely language (a whole)
- the mute 'mechanical course' of facts => through and with nature God/the divinity speaks


```python
prompt = f"""Complete the following phrase 'The walls stand speechless and cold that is to say...' with a maximum length of 50 tokens.
"""

print(prompt)
```

```python
# Versuch 
# Function to generate completions with different temperatures
#def generate_completions(prompt, model, temperatures):
    completions = {}
    for temp in temperatures:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=50,
            temperature=temp
        )
        completions[temp] = response.choices[0].text.strip()
    return completions

temperatures = [0.2, 0.4, 0.8, 1.0]
model = "gpt4o"  # Example model name

completions = generate_completions(prompt, model, temperatures)

#for temp, completion in completions.items():
    print(f"Temperature {temp}: {completion}")
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

```python
#Da mir die Keys fehlen, habe ich mit ChatGPT4o completions generiert. Eigentlich möchte ich bei dieser Abfrage aber die Outputs (Schritt 1) auswerten lassen. 

prompt = f"""
Consider the following completions for the phrase 'The walls stand speechless and cold that is to say...':

1. The emptiness echoes within the confines of their silence.
2. The void of communication fills the space they once occupied.
3. The air is thick with unspoken words and lingering shadows.
4. The silence screams louder than words ever could, enveloping everything in its icy grip.

Select the completion that best fits in the context of 
{poem_1.text}. 
Provide a brief explanation for your choice.
"""

print(prompt)
```

**"im Winde klirren die Fahnen"**


To analyze how different llms might interpret the phrase "im Winde klirren die Fahnen" based on the ambiguity of the word "Fahne" in German and English, we explore the various meanings provided and consider the contexts in which each might be used. 

Meanings of "Fahne" (Duden)
- Alkoholfahne (informal): Alcohol breath
- Printing (Druckwesen): Proof copy of a text not yet formatted into pages
- Hunting (Jägersprache): Long hair on the tails of certain hunting dogs and squirrels
- Zoology (Zoologie): Part of a bird's feather consisting of barbs on either side of the shaft
- Botany (Botanik): The uppermost petal of a butterfly flower
- Military: Service in the National People's Army of the GDR, historical use To call to arms (veraltet)

Meanings of flag (Oxford Learners Dictionaries)
- a piece of cloth with a special coloured design on it that may be the symbol of a particular country organization, may be used to give a signal or may have a particular meaning. A flag can be attached to a pole (= a long thin straight piece of wood or metal) or held in the hand.
- used to refer to a particular country or organization and its beliefs and values
- (verb) [transitive] flag something to draw attention to information that you think is important, especially by putting a special mark next to it
- (verb) [intransitive] to become tired, weaker or less enthusiastic

Prompt design
- zero-shot prompting (no context is given)
- few-shot prompting (minimal and rich context information: right and wrong context information, e.g. Add a paragraph describing a scene, such as a military parade or a hunting expedition.

Expected answers: 
- flags as weathercocks that move in the wind
- the speechlessness is interrupted by the clanging of the flags, the clanging stands for the "machine gait" of the world, and instead of the language of blossom, fruit and living being, the metal twisted by the wind sounds

```python
#zero-shot prompting
prompt = f"""
Extract the key meaning of the phrase 'the wind the flags clatter'. 
Describe in each case exactly what kind of flag this phrase renders.
""" 
print(prompt)
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

```python
#few-shot prompting
prompt: f"""Interpret the phrase 'im Winde klirren die Fahnen'. Here are some possible meanings for the word 'Fahne':

Military Context: Imagine a military parade where the flags of different units are clinking against their flagpoles in the wind.
Hunting Context: Consider a hunting expedition where the long hairs on the tails of hunting dogs are rustling in the wind.
Printing Context: Envision a scene in a printing house where proof copies of a text are fluttering as a breeze moves through the room.
Informal Context: Picture a scenario at a party where someone’s alcohol breath is noticeable as they talk in the wind.

Selecet the most possible context for {poem_1.text}. 
Provide a brief explanation for your choice.
"""
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

## Unsere Toten (1922)


**"die Füße mühn sich im zitternden Mondenschein"**


The hypothesis proposed by Liu et al. (2022), which asserts that the task of associating non-figurative language with its interpretation is more challenging than the reverse, will be tested using the phrase "die Füße mühn sich im zitternden Mondenschein". 

Interpretations: 
1.  A sense of effort or struggle illuminated by the unsteady light of the moon, perhaps hinting at a journey or hard work during the night.
2.  The phrase conveys an idea of toil and perseverance despite uncertain, ever-changing circumstances, symbolized by the trembling moonlight. The feet continue their arduous journey under the unsteady light of the moon.

Of particular interest:
- Can LLM generate poetical phrases based on paraphrases or interpretations?

Prompt design
- generate a phrase with 5-10 words rephrasing or extracting the key message of this interpretation
- persona and situation modeling
- contextual understanding
- “forward” and “backward” probabilities assigned to interpretations and phrases, respectively.

```python
prompt = f"""Regrettably, I have just experienced a mishap. 
A water bottle on my desk has tipped over, rendering some documents and various texts unreadable. However, I still possess interpretations of this phrase. 
Generate a suitable poetical phrase of 5-10 words in German that corresponds to the paraphrase. The phrase and its interpretation must align. The interpretation is ' A sense of effort or struggle illuminated by the unsteady light of the moon, perhaps hinting at a journey or hard work during the night.
The phrase conveys an idea of toil and perseverance despite uncertain, ever-changing circumstances, symbolized by the moonlight. The feet continue their arduous journey under the unsteady light of the moon.'

The poem is a contemporary poem entitled "Our Dead", which poetically reflects the experiences of the First World War.""" 

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

```python
# Kontext Gedicht, aber mit Lücken

prompt = f"""Regrettably, I have just experienced a mishap.
A water bottle on my desk has tipped over, rendering some documents and various texts unreadable. However, I still possess interpretations of this phrase and parts of the poem.

Poem:
Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, [...], vom Wandern
wund und zerfetzt, langsam bedächtig zur Erde gesetzt, [...]
tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden
Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage
schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!

Generate five poetical phrases of 5-10 words in German that corresponds to the paraphrase. The phrase and its interpretation must align. The interpretation is ' A sense of effort or struggle illuminated by the unsteady light of the moon, perhaps hinting at a journey or hard work during the night.
The phrase conveys an idea of toil and perseverance despite uncertain, ever-changing circumstances, symbolized by the moonlight. The feet continue their arduous journey under the unsteady light of the moon.'

The poem is a contemporary poem entitled "Our Dead", which poetically reflects the experiences of the First World War."""
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

**"wer hört eine Klage voll wilder Begehr"**

```python
prompt = f"""We want to understand the following poem: 

{poem_2.text}

What are possible meanings of the phrase 'wer hört eine Klage voll wilder Begehr'? Describe in each case exactly what kind of landscape this phrase renders.
"""

print(prompt)
```
