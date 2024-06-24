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


# Overall interpretation



In literary studies, 'interpretation' is understood as the interpretation of a literary text, especially with regard to the (transferred) meaning of the overall text. There are text-, author-, reader- and context-centered theories of literature and interpretation for the determination and identification of this overall meaning. 



Experiments: context windows

The context window determines the number of tokens the model can incorporate to predict the subsequent token.

Munkhdalai et al. (2024): "An effective memory system is crucial not just for comprehending long contexts with LLMs,
but also for reasoning, planning, continual adaptation for fresh knowledge, and even for
learning how to learn. This work introduces a close integration of compressive memory mod-
ule into the vanilla dot-product attention layer."

Challenges:  “needle-in-a-haystack” (Ivgi et al. 2023)

Context windows for our models: 
Llama3:70b = 8.2k
Gemini: 2M, 3000pages
Opus Claud: 200k
GPT4o: 128k

(Kosten! evtl. nur Llama 3:70b und GPt4o)

Could we force the LLM to say "this is the wrong context information"? Experiments with an unknown poem "Unsere Toten" (cf. text classification). 

Of particual interests: 
- studying how large and small context windows change the output
- studying how LLM deal with wrong context information
- determining the correct context information

Prompt design: 
- context files: large Wikipedia entries "Dungeon & Dragons" (51 Seiten, 17.300 Wörter) and "Vietnam War" (95 Seiten, 31.000 Wörter), World War II (83 Seiten, 26.300)


## Hälfte des Lebens



```python
### Llama3:70b
```

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

```python
## Unsere Toten

Wrong context

prompt = f"""Read the following context information in pdf, extract the key features then interpret the following poem: 'Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern 
wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos 
tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden 
Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage 
schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!' Does this poem belong this context?"""
print (prompt)
```

```python
prompt = f"""why does this context does not fit to this poem?"""
print (prompt)
```

Which context is more likely?
prompt = f"""Read the following Wikipedia entries on World War I and II, extract three key features, then determine which contextual information is correct for the interpretation of the poem: Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern 
wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos 
tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden 
Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage 
schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!'"""

print (prompt)


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

Wrong context (still prompting with ChatGPT-4o)


[...] The poem provided does not directly belong to the context of the Vietnam War as described in the context file. However, it shares themes that can be broadly applicable to the experiences of war, displacement, and the human suffering resulting from such conflicts. Here's how the poem's themes might be loosely related to the context of the Vietnam War:

Displacement and Suffering:

The Vietnam War caused significant displacement, with millions of Vietnamese becoming refugees. The poem's imagery of tired feet and wandering could metaphorically represent the experiences of these refugees who traveled from various parts of Vietnam and other affected regions.
Nighttime and Fear:

The Vietnam War created an atmosphere of fear and uncertainty, much like the nighttime setting described in the poem. The "trembling moonlight" might evoke the fear and anxiety experienced during bombings and military operations.
Call for Remembrance:

The plea to not be forgotten ("nur nicht vergessen! Uns nicht vergessen!") resonates with the experiences of many war survivors and veterans who seek recognition and remembrance for their sacrifices and suffering. This is relevant to the context of the Vietnam War, where many veterans and civilians continue to seek acknowledgment for their experiences.
Journey Towards Safety:

Just as the poem describes a journey "deep into Germany," the refugees of the Vietnam War embarked on perilous journeys seeking safety and a new life, often in other countries. This reflects the universal search for peace and stability following a conflict.
In summary, while the poem does not specifically reference the Vietnam War, its themes of displacement, suffering, fear, and the need for remembrance can be applied to the experiences of those affected by the Vietnam War. The emotional and psychological impact of war described in the poem can be seen as a universal reflection of the human condition in times of conflict.
[...]


The poem and the context provided do not fit together primarily because of the specific historical and geographical references they each entail. Here’s a more detailed explanation:

Geographical and Cultural Context:

The poem references Germany explicitly ("tief nach Deutschland hinein"), suggesting a European context. It evokes imagery and experiences tied to a European setting, which could relate to historical events such as World War II or the aftermath of that war, involving displaced persons and refugees within Europe.
The Vietnam War, on the other hand, is a conflict set in Southeast Asia, involving North and South Vietnam, the United States, and various other allies and adversaries. The geographical and cultural context of the Vietnam War is distinctly different from that of Germany and Europe.
Historical Events:

The historical events described in the context file are specific to the Vietnam War: the conflict between North and South Vietnam, the involvement of international powers like the United States, the military strategies employed, and the political developments leading to the eventual fall of Saigon.
The poem’s themes of wandering, displacement, and a plea for remembrance might resonate with any conflict, but its references to moving "deep into Germany" suggest a post-World War II European refugee crisis rather than the events of the Vietnam War.
Symbolism and Imagery:

The poem uses imagery such as "tired feet," "wounded from wandering," and "trembling moonlight," which could symbolize the weariness and suffering of people affected by war. While these themes are universal, the symbolic journey "deep into Germany" is specific and not reflective of the journeys undertaken by Vietnamese refugees or soldiers.
The Vietnam War context involves specific symbols and imagery such as jungle warfare, helicopter insertions, and the Ho Chi Minh trail, which are absent from the poem.
Historical and Political Context:

The poem’s context seems more aligned with the post-World War II period, focusing on the experiences of people displaced within Europe, particularly those moving towards or within Germany.
The Vietnam War’s context involves Cold War dynamics, guerrilla warfare, and the political struggle between communism and anti-communism in Southeast Asia. The political and military strategies, the involvement of superpowers, and the specific experiences of the Vietnamese people during this period do not align with the poem's focus.
Summary:
While the themes of displacement, suffering, and remembrance are universal and could apply to various conflicts, the specific references and imagery in the poem do not fit the historical and geographical context of the Vietnam War. The poem appears to be more closely related to European experiences, particularly those associated with World War II and its aftermath, rather than the specific events and circumstances of the Vietnam War.


Determining context: World War II (still prompting with ChatGPT-4o)


The poem aligns more closely with World War II due to several contextual elements:

Restlessness and Return: The sense of movement towards Germany and the plea for remembrance are reminiscent of the millions displaced or returning home after the war, a common scenario post-World War II due to widespread destruction and shifting borders.
Humanitarian Focus: The emotional plea to not be forgotten ties in with the massive humanitarian crises and the memory of the Holocaust, emphasizing the importance of remembering those who suffered.
Thus, while both World Wars involved significant human movement and suffering, the specific context of post-war displacement and the plea for remembrance strongly suggest that this poem belongs to the context of World War II.


### Opus

```python
%%ai opus
{prompt}
```
