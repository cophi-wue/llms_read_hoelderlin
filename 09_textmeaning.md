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

# Einstellungen setzen
temperature = 0.8
system_prompt = "You are an expert in German literature and you are addressing other experts in German literature. You answer the questions truthfully and short."

settings(system_prompt, temperature)

```

```python
#defining aliases
init_gemini()

model =  ollama3()
#%ai register llama3big model

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model
```

# Text meaning



## Hölderlin: Hälfte des Lebens


**TASK 1: General Knowledge**

```python
#Reproduction
prompt = f"""We want to understand the following poem: 

{poem_1.text}

Given the poem: [...] Provide a structured summary of the central content of the poem. Identify the main themes, motifs, and lyrical personas. Describe the atmosphere of the poem in your own words, and outline the key relationships or events depicted. Finally, define a relevant literary term that plays a central role in the poem and explain its significance for understanding the text.
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
#Reorganziation and Transfer
prompt = f"""We want to understand the following poem: 

{poem_1.text}

Given the poem: [...] Examine the stylistic devices used in the poem and analyze their effect on the interpretation of its central themes. Situate the poem within its literary and historical context and explain how its linguistic features support the poet’s intended message. Draw connections between the poem’s ideas and a comparable literary or historical aspect. Finally, discuss whether the poem effectively communicates its message and justify your evaluation.
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
#Reflection and Problem-Solving
prompt = f"""We want to understand the following poem: 

{poem_1.text}

Given the poem: [...] Interpret the poem by analyzing the interaction between its central themes, motifs, and linguistic features. Assess the aesthetic quality and relevance of the poem with respect to contemporary or universal issues. Critically evaluate the worldview or message conveyed by the poem, providing a well-supported argument for your perspective. Finally, develop a creative or alternative interpretation of the poem and explain the reasoning behind your approach.
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

**TASK 2: Expert knowledge (Theses and questions from Hölderlin research)**

```python
#Theoriegeleitete Interpretationen (Forschungsthese Görner 2016, S. 107 "Aber mit postkolonialer Literaturforschung bringt man es nicht weit bei der Erschließung dieses [Hölderlins] Werkes. (Post-)Strukturalistenund Dekonstruktivisten scheint Hölderlin dagegen – wennauch absichtslos – vorgearbeitet zu haben."
# Studying representativeness, steerability, consistency of literary and cultural theories 
prompt = f"""We want to understand the following poem: 

{poem_1.text}

Given the poem: [...] 1. Provide an interpretation and interpretation hypotheses of the poem (150-200 words) from three distinct literary theoretical perspectives: Hermeneutic, Poststructuralist, and Postkolonial theory. 2. After generating the interpretations, rank them by their plausibility in effectively representing each  theoretical framework. Discuss which theory is better emulated by the LLM and explain the reasons for this ranking, considering key theoretical assumptions and the specific aspects of the poem that support each interpretation.
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

**TASK 3: Abstraction and Transfer**


Counterfactual Meaning-production
Implicit rule: Only words with an odd number of syllables carry meaning

```python
prompt = f"""Read the following interpretations of poem 1 and poem 2. Then infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem Hälfte des Lebens:
{poem_1.text}

Poem 1
Helga M. Novak (1935–2013): HÄUSER (1982)
Landschaft Erde Natur
alles weiblich
dahin will ich gehen
wo es trostlos ist
dahin will ich gehen
wo nichts ist
Natur und unangetastet
und werde in aller Stille
ein Haus bauen
ein Haus beziehen
und werde es – ungeliebt
und unfähig zu lieben –
mit meiner maßlosen
Liebe entzünden
auch diese Nacht geht vorbei
und keiner kommt
und reißt meine Zäune ein
siehst du die gelbe verrostete Bank
auf der werde ich sitzen
wenn ich nicht weiter weiß
also für immer wie eine
der die Augen übergegangen sind

Interpretation of the poem 1: 
The poem reveals key themes of isolation, purity, and existential yearning. The analysis highlights several layers of meaning:

Nature as Refuge:
Odd-syllable words like "Landschaft," "Natur," and "unangetastet" emphasize the speaker’s desire for a sanctuary in the natural world—one untouched by external interference. This underscores the motif of withdrawal and self-containment.

Paradox of Love and Isolation:
The words "maßlosen," "ein," and "eine" highlight the tension between boundless emotional capacity and the inability to connect. This paradox is central to the speaker's journey, where love becomes both a source of meaning and an agent of isolation.

Timelessness and Despair:
Words like "auch" and "auf" contribute to a tone of inevitability and timelessness. The "verrostete Bank" (rusted bench) symbolizes stasis and resignation, while the repetition of singular pronouns reflects the permanence of solitude.

Poem 2:
Nikolaus Lenau (1802–1850): Einsamkeit. (1834)
Wild verwachsne dunkle Fichten,
Leise klagt die Quelle fort;
Herz, das ist der rechte Ort
Für dein schmerzliches Verzichten!
Grauer Vogel in den Zweigen!
Einsam deine Klage singt,
Und auf deine Frage bringt
Antwort nicht des Waldes Schweigen.
Wenn’s auch immer schweigen bliebe,
Klage, klage fort; es weht,
Der dich höret und versteht,
Stille hier der Geist der Liebe.
Nicht verloren hier im Moose,
Herz, dein heimlich Weinen geht,
Deine Liebe Gott versteht,
Deine tiefe, hoffnungslose!

Interpreation of Poem 2:
The poem creates a thematic pattern focused on the interplay between solitude, unanswered longing, and emotional expression within nature. Key interpretative insights include:

Nature as a Mirror of Solitude:
The words "Fichten" and "Moose" evoke an unchanging natural world, which mirrors the speaker’s sense of stasis and isolation. The setting becomes a sanctuary where the speaker's sorrow is both reflected and held.

Sorrow as a Persistent Companion:
The repetition of "Klage" (lament) and the presence of "Frage" (question) suggest an endless cycle of sorrow and yearning. Despite the lack of answers, the act of lamenting itself carries meaning and reflects the speaker’s resilience.

The Divine as Silent Witness:
The speaker’s "Weinen" (crying) and hidden emotions are juxtaposed with their connection to God ("deine Liebe Gott versteht"). This relationship introduces a spiritual dimension to the speaker’s suffering, where even unspoken sorrow is acknowledged.
"""

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
# Two examples, unknown rule "the meaning of an expression lies solely in its function within an act of communication, independent of any direct connection to an external reality."
prompt = f"""Read the following interpretations of poem 1 and poem 2. Then infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem Hälfte des Lebens:
{poem_1.text}

Poem 1
Helga M. Novak (1935–2013): HÄUSER (1982)
Landschaft Erde Natur
alles weiblich
dahin will ich gehen
wo es trostlos ist
dahin will ich gehen
wo nichts ist
Natur und unangetastet
und werde in aller Stille
ein Haus bauen
ein Haus beziehen
und werde es – ungeliebt
und unfähig zu lieben –
mit meiner maßlosen
Liebe entzünden
auch diese Nacht geht vorbei
und keiner kommt
und reißt meine Zäune ein
siehst du die gelbe verrostete Bank
auf der werde ich sitzen
wenn ich nicht weiter weiß
also für immer wie eine
der die Augen übergegangen sind

Interpretation from poem 1: 
Under this analytical rule, the poem is understood as a communicative act between the speaker and themselves or an imagined other, rather than a description of an external world. The expressions function to construct an internal landscape where themes of isolation, paradoxical love, and existential endurance are explored. The speaker builds symbolic spaces (house, bench) to house their emotional turmoil, creating a self-contained dialogue within a desolate yet meaningful internal world. This interpretation highlights the poem’s focus on the subjective function of language and its power to shape emotional reality.

Poem 2: 
Nikolaus Lenau (1802–1850): Einsamkeit. (1834)
Wild verwachsne dunkle Fichten,
Leise klagt die Quelle fort;
Herz, das ist der rechte Ort
Für dein schmerzliches Verzichten!
Grauer Vogel in den Zweigen!5
Einsam deine Klage singt,
Und auf deine Frage bringt
Antwort nicht des Waldes Schweigen.
Wenn’s auch immer schweigen bliebe,
Klage, klage fort; es weht,10
Der dich höret und versteht,
Stille hier der Geist der Liebe.
Nicht verloren hier im Moose,
Herz, dein heimlich Weinen geht,
Deine Liebe Gott versteht,15
Deine tiefe, hoffnungslose!

Interpretation from poem 2:
The poem emerges as an exploration of solitude and sorrow, where the act of communication itself—through lament, introspection, and spiritual dialogue—becomes the primary source of meaning. The expressions function to externalize the speaker’s inner turmoil, transforming nature into a reflective space and God into an empathetic listener.

Under this analysis, the poem suggests that even in the absence of a response from the external world, the act of expressing sorrow has intrinsic value, as it connects the speaker to a spiritual dimension and validates their inner experience. This highlights the resilience of the human spirit in finding meaning through communication, even in the face of silence and hopelessness.
"""
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

## Unsere Toten


**TASK 1: General Knowledge**

```python
#Reproduction
prompt = f"""We want to understand the following poem: 

Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!

Given the poem: [...] Provide a structured summary of the central content of the poem. Identify the main themes, motifs, and lyrical personas. Describe the atmosphere of the poem in your own words, and outline the key relationships or events depicted. Finally, define a relevant literary term that plays a central role in the poem and explain its significance for understanding the text.
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

```

```python
#Reorganziation and Transfer
prompt = f"""We want to understand the following poem: 

Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!


Given the poem: [...] Examine the stylistic devices used in the poem and analyze their effect on the interpretation of its central themes. Situate the poem within its literary and historical context and explain how its linguistic features support the poet’s intended message. Draw connections between the poem’s ideas and a comparable literary or historical aspect. Finally, discuss whether the poem effectively communicates its message and justify your evaluation.
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
#Reflection and Problem-Solving
prompt = f"""We want to understand the following poem: 

Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!

Given the poem: [...] Interpret the poem by analyzing the interaction between its central themes, motifs, and linguistic features. Assess the aesthetic quality and relevance of the poem with respect to contemporary or universal issues. Critically evaluate the worldview or message conveyed by the poem, providing a well-supported argument for your perspective. Finally, develop a creative or alternative interpretation of the poem and explain the reasoning behind your approach.
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

**TASK 2: Expert knowledge (Theses and questions from research)**


```python
#Theoriegeleitete Interpretationen
# Studying representativeness, steerability, consistency of literary and cultural theories 
prompt = f"""We want to understand the following poem: 

Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!

Given the poem: [...] 1. Provide an interpretation and interpretation hypotheses of the poem (150-200 words) from three distinct literary theoretical perspectives: Hermeneutic, Poststructuralist, and Postkolonial theory. 2. After generating the interpretations, rank them by their plausibility in effectively representing each  theoretical framework. Discuss which theory is better emulated by the LLM and explain the reasons for this ranking, considering key theoretical assumptions and the specific aspects of the poem that support each interpretation.
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

**TASK 3: Abstraction and Transfer**


```python
# Two examples, unknown rule "only words with an odd number of syllables carry meaning"

prompt = f"""Read the following interpretations of poem 1 and poem 2. Then infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the following poem 3 "Unsere Toten":

Poem 1
Helga M. Novak (1935–2013): HÄUSER (1982)
Landschaft Erde Natur
alles weiblich
dahin will ich gehen
wo es trostlos ist
dahin will ich gehen
wo nichts ist
Natur und unangetastet
und werde in aller Stille
ein Haus bauen
ein Haus beziehen
und werde es – ungeliebt
und unfähig zu lieben –
mit meiner maßlosen
Liebe entzünden
auch diese Nacht geht vorbei
und keiner kommt
und reißt meine Zäune ein
siehst du die gelbe verrostete Bank
auf der werde ich sitzen
wenn ich nicht weiter weiß
also für immer wie eine
der die Augen übergegangen sind

Interpretation of the poem 1: 
The poem reveals key themes of isolation, purity, and existential yearning. The analysis highlights several layers of meaning:

Nature as Refuge:
Odd-syllable words like "Landschaft," "Natur," and "unangetastet" emphasize the speaker’s desire for a sanctuary in the natural world—one untouched by external interference. This underscores the motif of withdrawal and self-containment.

Paradox of Love and Isolation:
The words "maßlosen," "ein," and "eine" highlight the tension between boundless emotional capacity and the inability to connect. This paradox is central to the speaker's journey, where love becomes both a source of meaning and an agent of isolation.

Timelessness and Despair:
Words like "auch" and "auf" contribute to a tone of inevitability and timelessness. The "verrostete Bank" (rusted bench) symbolizes stasis and resignation, while the repetition of singular pronouns reflects the permanence of solitude.

Poem 2:
Nikolaus Lenau (1802–1850): Einsamkeit. (1834)
Wild verwachsne dunkle Fichten,
Leise klagt die Quelle fort;
Herz, das ist der rechte Ort
Für dein schmerzliches Verzichten!
Grauer Vogel in den Zweigen!
Einsam deine Klage singt,
Und auf deine Frage bringt
Antwort nicht des Waldes Schweigen.
Wenn’s auch immer schweigen bliebe,
Klage, klage fort; es weht,
Der dich höret und versteht,
Stille hier der Geist der Liebe.
Nicht verloren hier im Moose,
Herz, dein heimlich Weinen geht,
Deine Liebe Gott versteht,
Deine tiefe, hoffnungslose!

Interpreation of Poem 2:
The poem creates a thematic pattern focused on the interplay between solitude, unanswered longing, and emotional expression within nature. Key interpretative insights include:

Nature as a Mirror of Solitude:
The words "Fichten" and "Moose" evoke an unchanging natural world, which mirrors the speaker’s sense of stasis and isolation. The setting becomes a sanctuary where the speaker's sorrow is both reflected and held.

Sorrow as a Persistent Companion:
The repetition of "Klage" (lament) and the presence of "Frage" (question) suggest an endless cycle of sorrow and yearning. Despite the lack of answers, the act of lamenting itself carries meaning and reflects the speaker’s resilience.

The Divine as Silent Witness:
The speaker’s "Weinen" (crying) and hidden emotions are juxtaposed with their connection to God ("deine Liebe Gott versteht"). This relationship introduces a spiritual dimension to the speaker’s suffering, where even unspoken sorrow is acknowledged.

Poem 3: 
"Unsere Toten"
Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!
"""

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
## Two examples, unknown rule "the meaning of an expression lies solely in its function within an act of communication, independent of any direct connection to an external reality."
prompt = f"""Read the following interpretations of poem 1 and poem 2. Then infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the following poem 3 "Unsere Toten":

Poem 1
Helga M. Novak (1935–2013): HÄUSER (1982)
Landschaft Erde Natur
alles weiblich
dahin will ich gehen
wo es trostlos ist
dahin will ich gehen
wo nichts ist
Natur und unangetastet
und werde in aller Stille
ein Haus bauen
ein Haus beziehen
und werde es – ungeliebt
und unfähig zu lieben –
mit meiner maßlosen
Liebe entzünden
auch diese Nacht geht vorbei
und keiner kommt
und reißt meine Zäune ein
siehst du die gelbe verrostete Bank
auf der werde ich sitzen
wenn ich nicht weiter weiß
also für immer wie eine
der die Augen übergegangen sind

Interpretation from poem 1: 
Under this analytical rule, the poem is understood as a communicative act between the speaker and themselves or an imagined other, rather than a description of an external world. The expressions function to construct an internal landscape where themes of isolation, paradoxical love, and existential endurance are explored. The speaker builds symbolic spaces (house, bench) to house their emotional turmoil, creating a self-contained dialogue within a desolate yet meaningful internal world. This interpretation highlights the poem’s focus on the subjective function of language and its power to shape emotional reality.

Poem 2: 
Nikolaus Lenau (1802–1850): Einsamkeit. (1834)
Wild verwachsne dunkle Fichten,
Leise klagt die Quelle fort;
Herz, das ist der rechte Ort
Für dein schmerzliches Verzichten!
Grauer Vogel in den Zweigen!5
Einsam deine Klage singt,
Und auf deine Frage bringt
Antwort nicht des Waldes Schweigen.
Wenn’s auch immer schweigen bliebe,
Klage, klage fort; es weht,10
Der dich höret und versteht,
Stille hier der Geist der Liebe.
Nicht verloren hier im Moose,
Herz, dein heimlich Weinen geht,
Deine Liebe Gott versteht,15
Deine tiefe, hoffnungslose!

Interpretation from poem 2:
The poem emerges as an exploration of solitude and sorrow, where the act of communication itself—through lament, introspection, and spiritual dialogue—becomes the primary source of meaning. The expressions function to externalize the speaker’s inner turmoil, transforming nature into a reflective space and God into an empathetic listener.

Under this analysis, the poem suggests that even in the absence of a response from the external world, the act of expressing sorrow has intrinsic value, as it connects the speaker to a spiritual dimension and validates their inner experience. This highlights the resilience of the human spirit in finding meaning through communication, even in the face of silence and hopelessness.

Poem 3: 
"Unsere Toten"
Von Westen und Osten, von Nord und Süd schleppen sich nächtens viele Füße müd, Füße, vom Wandern wund und zerfetzt, langsam bedächtig zur Erde gesetzt, müh'n sich im zitternden Mondenschein rastlos tief nach Deutschland hinein. Und wer mit lauschendem Ohr noch wacht hört sie in jedweder werdenden Nacht, hört dies Schlurfen so müde und schwer, hört eine Klage voll wilder Begehr, eine Klage schmerzzerfressen: nur nicht vergessen! Uns nicht vergessen!
"""
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

```
