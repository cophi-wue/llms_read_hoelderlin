---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.6
  kernelspec:
    display_name: llm_env
    language: python
    name: llm_env
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

# Hälfte des Lebens

```python
#defining aliases
init_gemini()

#model =  ollama3()
#%ai register llama3big model

model =  gpt4()
%ai register gpt4o model

# note that "opus" always refers to Anthropic's model "sonnet".

model = opus()
%ai register opus model
```


# Assonanzen 
## Task 1: Student communication: simple identification task: Detect assonances
### 1.a: Detection based on different definitions of assonance
### 1.b: Detection based on a two-step CoT-prompt: 1) Translate to IPA, 2) then perform assonance detection
### 1.c: Same tasks for English¶

## Expectation:
- Definitionsabhängigkeit: Je genauer der Laut-und Phonemcharakter erläutert wird, desto besser die Erkennung Assonanzen
- Schiwerigkeiten, die richtigen Laute im Deutschen zu erkennen. 

```python
assonance = """Assonance is a similarity in sound between two stressed syllables 
that are close together in a text, created by the same vowels but different consonants """

assonance02 = """Assonance is the repetition of identical or similar phonemes in words or syllables that occur close together
in terms of their vowel phonemes (e.g. lean green meat)"""

assonance03 = """Assonance is the repetition of identical or similar phonemes between two stressed syllables that occur close together
in terms of their vowel phonemes (e.g. lean green meat). Note that identical vowels do not always imply same phonems. 
The 'o'-sound in 'often' and 'other' does not produce the same phonem"""
```

```python
prompt01 = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.text} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt02 = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.text} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt03 = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.text} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt04_ipa = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.text} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use a two-step reasoning: Firstly, translate the poem to IPA. Secondly, perform the requested analysis of assonances based on the IPA-translation.
Use the following form in the second step of your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt_en01 = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'The light of the fire is a sight.' - the long 'i' sound in 'light', 'fire, and 'sight' creates assonance."""

prompt_en02 = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'The light of the fire is a sight.' - the long 'i' sound in 'light', 'fire, and 'sight' creates assonance."""


prompt_en03 = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'The light of the fire is a sight.' - the long 'i' sound in 'light', 'fire, and 'sight' creates assonance."""

prompt04en_ipa = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_1.translations[0]} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use a two-step reasoning: Firstly, translate the poem to IPA. Secondly, perform the requested analysis of assonances based on the IPA-translation.
Use the following form in your answer: 'The light of the fire is a sight.' - the long 'i' sound (IPA: aɪ) in 'light', 'fire, and 'sight' creates assonance."""
```

## Task 1.a

```python
print(prompt01)
```

## Gold-Standard: alle Assonanzen:
### Stanza 1
Z 1: Mit / Birnen

Z 1: gelben / hänget

Z 2: mit / wilden

Z 3: den / See

Z 4: Und / trunken ( + Z 5  Tunkt)

Z 5 (s. 4 tunkt) 

Z 6

Z 7

### Stanza 2

Z. 8 Weh / nehm

Z. 8 Winter / ist

Z 9. - 

Z 10 - 

Z 11 der / Erde

Z 12 -

Z 13 - Winde (bis Z. 14 Klirren)

Z. 14 

```python
%%ai gpt4o
{prompt01}
```

```python
print(prompt02)
```

```python
%%ai gpt4o
{prompt02}
```

```python
print(prompt03)
```

```python
%%ai gpt4o
{prompt03}
```

```python
%%ai gpt4o
{prompt04_ipa}
```

```python
print(prompt_en01)
```

Assonances gold standard englisch

l 1: yellow / pears
l 2: -
l 3: land / hangs / lake
l 4 o / lovely 
l5 with kisses
l 6 you your
l 7 -

l 8 alas / shall (naja)
l 9 when / where
l 10 - 
l11 and / shadows 
l 12 
l 13 in / wind
l 14 waether/vanes/clatter


```python
%%ai gpt4o
{prompt_en01}
```

```python
print(prompt_en02)
```

```python
%%ai gpt4o
{prompt_en02}
```

```python
print(prompt_en03)
```

```python
%%ai gpt4o
{prompt_en03}
```

```python
%%ai gpt4o
{prompt04en_ipa}
```

```python
print(prompt01)

printmd(gemini(prompt01))
```

```python
printmd(gemini({prompt02}))
```

```python
printmd(gemini(prompt03))
```

```python
printmd(gemini(prompt04_ipa))
```

```python
printmd(gemini(prompt_en01))
```

```python
printmd(gemini(prompt_en02))
```

```python
printmd(gemini(prompt_en03))
```

```python
print(prompt04en_ipa)
```

```python
printmd(gemini(prompt04en_ipa))
```

```python
print(prompt01)
```

```python
%%ai opus
{prompt01}
```

```python
%%ai opus
{prompt02}
```

```python
%%ai opus
{prompt03}
```

```python
print(prompt_en01)
```

```python
%%ai opus
{prompt_en01}
```

```python
%%ai opus
{prompt_en02}
```

```python
%%ai opus
{prompt_en03}
```

# Task 2: Epert communication: interpretation based on assonances


```python
prompt_expert = f"""Perform the following task in two steps. 
Step 1: {prompt04_ipa}
Step 2: Based on step 1, give an interpretation of the poem that takes into account the connections and contrast between the semantic fields that 
are grouped by the different assonances.
"""

```

```python
%%ai gpt4o
{prompt_expert}
```

```python
printmd(gemini(prompt_expert))
```

```python
%%ai opus
{prompt_expert}
```

# Task 3: Abstraction-Transfer
## 3.a Counterfactual Assonances: The notion of "eusonance": Detecting eusonances

```python
eusonance = """Eusonance occurs when the vowel sounds of the stressed syllables in two consecutive words in the same line are a German i-sound and a German e-sound. 
The order between the i sound and the e sound does not matter.
Monosyllabic words always count as words with a stressed syllable
(e.g. "Ich" and "esse" in "Ich esse Kuchen")."""
```

```python
prompt_eusonance = f"""Here is a definition of Eusonance: {eusonance}. 
Using this definition, give a full description of all eusonances in this poem: \n {poem_1.text} \n
Explain in each case the eusonance by repeating the words and by giving the common vowel not in IPA but in normal latin letters.
Use a two-step reasoning: Firstly, translate the poem to IPA. Secondly, perform the requested analysis of eusonances based on the IPA-translation.
Use the following form in the second step of your answer: 'Nichts ereignet sich' - the 'i' sound and the 'e' sound in 'Nichts' and 'ereignet' create eusonance."""
```

### gold standard eusonance

Z. 1 Mit Gelben 

Z. 3 in den

Z. 8 ich wenn



```python
%%ai gpt4o
{prompt_eusonance}
```

```python
printmd(gemini(prompt_eusonance))
```

```python
%%ai opus
{prompt_eusonance}
```

## 3b: Inference of implicit rule and rule application

implicit rule: find the two main assonance vowels and identify the central semantic field that connects both groups and the central semantic field constituing a central opposition.

```python
prompt_transfer = f"""
Given the following definition: {assonance03}, 
infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem with the title "Hälfte des Lebens": 
{poem_1.text}.

Here is the poem: Waldgespräch (1815)
Es ist schon spät, es wird schon kalt,
Was reit’st du einsam durch den Wald?
Der Wald ist lang, du bist allein,
Du schöne Braut! Ich führ’ dich heim!

„Groß ist der Männer Trug und List,
Vor Schmerz mein Herz gebrochen ist,
Wohl irrt das Waldhorn her und hin,
O flieh! Du weißt nicht, wer ich bin.“

So reich geschmückt ist Roß und Weib,
So wunderschön der junge Leib,
Jetzt kenn’ ich dich – Gott steh’ mir bei!
Du bist die Hexe Lorelei.

„Du kennst mich wohl – von hohem Stein
Schaut still mein Schloß tief in den Rhein.
Es ist schon spät, es wird schon kalt,
Kommst nimmermehr aus diesem Wald!“


In this poem, the two central assonances are the "a"-Laut in words like "Wald" and "kalt" on the one hand and the "ei"-Laut
in words like "Lorelei", "Rhein", "Weib", "reiten", "heim". Both groups are connected by the semantic of "Wald" and "Rhein" is
natural environments (forest as type of nature, the Rhein as an instance of a river), both being also symbols of 
the contemporary construction of national German identity in Romanticism. Lorelei as a personification of attraction and fatality is 
in this poem finally transferred to the imagination of the forest, which is, at the beginning of the poem, introduced as a harmless locus of
romantic loneliness. So, one of the word groups that are grouped by assonance (here: "ei") affects the meaning of the other group (here "a").

"""
```

```python
printmd(gemini(prompt_transfer))
```

```python
%%ai gpt4o
{prompt_transfer}
```

```python
%%ai opus
{prompt_transfer}
```

```python

```

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

# Unsere Toten

```python
#defining aliases
init_gemini()

#model =  ollama3()
#%ai register llama3big model

model =  gpt4()
%ai register gpt4o model

model = opus()
%ai register opus model
```


# Assonanzen 
## Task 1: Student communication: simple identification task: Detect assonances
### 1.a: Detection based on different definitions of assonance
### 1.b: Detection based on a two-step CoT-prompt: 1) Translate to IPA, 2) then perform assonance detection
### 1.c: Same tasks for English¶

## Expectation:
- Definitionsabhängigkeit: Je genauer der Laut-und Phonemcharakter erläutert wird, desto besser die Erkennung Assonanzen
- Schiwerigkeiten, die richtigen Laute im Deutschen zu erkennen. 

```python
assonance = """Assonance is a similarity in sound between two stressed syllables 
that are close together in a text, created by the same vowels but different consonants """

assonance02 = """Assonance is the repetition of identical or similar phonemes in words or syllables that occur close together
in terms of their vowel phonemes (e.g. lean green meat)"""

assonance03 = """Assonance is the repetition of identical or similar phonemes between two stressed syllables that occur close together
in terms of their vowel phonemes (e.g. lean green meat). Note that identical vowels do not always imply same phonems. 
The 'o'-sound in 'often' and 'other' does not produce the same phonem"""
```

```python
prompt01 = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt02 = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt03 = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt04_ipa = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.text} \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use a two-step reasoning: Firstly, translate the poem to IPA. Secondly, perform the requested analysis of assonances based on the IPA-translation.
Use the following form in the second step of your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt_en01 = f"""Here is a definition of assonance: {assonance}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""


prompt_en02 = f"""Here is a definition of assonance: {assonance02}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""

prompt_en03 = f"""Here is a definition of assonance: {assonance03}. 
Using this definition, give a full description of all assonances in this poem: \n {poem_2.translations[0]}. \n
Explain in each case the assonance by repeating the words and by giving the common vowel.
Use the following form in your answer: 'Dem Nordmann schwinden die Sorgen' - the 'o' sound in 'Nordmann' and 'Sorgen' creates assonance."""
```

## Task 1.a

```python
print(prompt01)
```

```python
%%ai gpt4o
{prompt01}
```

```python
print(prompt02)
```

```python
%%ai gpt4o
{prompt02}
```

```python
print(prompt03)
```

```python
%%ai gpt4o
{prompt03}
```

```python
print(prompt_en01)
```

```python
%%ai gpt4o
{prompt_en01}
```

```python
print(prompt_en02)
```

```python
%%ai gpt4o
{prompt_en02}
```

```python
print(prompt_en03)
```

```python
%%ai gpt4o
{prompt_en03}
```

```python
print(prompt01)

printmd(gemini(prompt01))
```

```python
printmd(gemini({prompt02}))
```

```python
printmd(gemini(prompt03))
```

```python
printmd(gemini(prompt_en01))
```

```python
printmd(gemini(prompt_en02))
```

```python
printmd(gemini(prompt_en03))
```

```python
%%ai opus
{prompt01}
```

```python
%%ai opus
{prompt02}
```

```python
%%ai opus
{prompt03}
```

```python
%%ai opus
{prompt_en01}
```

```python
%%ai opus
{prompt_en02}
```

```python
%%ai opus
{prompt_en03}
```

# Task 2: Epert communication: interpretation based on assonances

```python
prompt_expert = f"""Perform the following task in two steps. 
Step 1: {prompt04_ipa}
Step 2: Based on step 1, give an interpretation of the poem that takes into account the connections and contrast between the semantic fields that 
are grouped by the different assonances.
"""
```

```python
%%ai gpt4o
{prompt_expert}
```

```python
printmd(gemini(prompt_expert))
```

```python
%%ai opus
{prompt_expert}
```

# Task 3: Abstraction-Transfer
## 3.a Counterfactual Assonances: The notion of "eusonance": Detecting eusonances

```python
eusonance = """Eusonance occurs when the vowel sounds of the stressed syllables in two consecutive words in the same line are a German i-sound and a German e-sound. 
The order between the i sound and the e sound does not matter.
Monosyllabic words always count as words with a stressed syllable
(e.g. "Ich" and "esse" in "Ich esse Kuchen")."""
```

```python
prompt_eusonance = f"""Here is a definition of Eusonance: {eusonance}. 
Using this definition, give a full description of all eusonances in this poem: \n {poem_2.text} \n
Explain in each case the eusonance by repeating the words and by giving the common vowel.
Use a two-step reasoning: Firstly, translate the poem to IPA. Secondly, perform the requested analysis of eusonances based on the IPA-translation.
Use the following form in the second step of your answer: 'Dem Nichts schwindet die Sorge' - the 'i' sound and the 'e' sound in 'Dem' and 'Nichts' creates eusonance."""
```

# gold standard eusonance
Z. 2 sich nächtens 
Z. 7 in jedweden
Z. 12 nicht vergessen



```python
%%ai gpt4o
{prompt_eusonance}
```

```python
printmd(gemini(prompt_eusonance))
```

```python
%%ai opus
{prompt_eusonance}
```

## 3b: Inference of implicit rule and rule application

implicit rule: find the two main assonance vowels and identify the central semantic field that connects both groups and the central semantic field constituing a central opposition.

```python
prompt_transfer = f"""

Given the following definition: {assonance03}, 

infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem with the title "Unsere Toten": 
{poem_2.text}.

Here is the poem: Waldgespräch (1815)
Es ist schon spät, es wird schon kalt,
Was reit’st du einsam durch den Wald?
Der Wald ist lang, du bist allein,
Du schöne Braut! Ich führ’ dich heim!

„Groß ist der Männer Trug und List,
Vor Schmerz mein Herz gebrochen ist,
Wohl irrt das Waldhorn her und hin,
O flieh! Du weißt nicht, wer ich bin.“

So reich geschmückt ist Roß und Weib,
So wunderschön der junge Leib,
Jetzt kenn’ ich dich – Gott steh’ mir bei!
Du bist die Hexe Lorelei.

„Du kennst mich wohl – von hohem Stein
Schaut still mein Schloß tief in den Rhein.
Es ist schon spät, es wird schon kalt,
Kommst nimmermehr aus diesem Wald!“


In this poem, the two central assonances are the "a"-Laut in words like "Wald" and "kalt" on the one hand and the "ei"-Laut
in words like "Lorelei", "Rhein", "Weib", "reiten", "heim". Both groups are connected by the semantic of "Wald" and "Rhein" is
natural environments (forest as type of nature, the Rhein as an instance of a river), both being also symbols of 
the contemporary construction of national German identity in Romanticism. Lorelei as a personification of attraction and fatality is 
in this poem finally transferred to the imagination of the forest, which is, at the beginning of the poem, introduced as a harmless locus of
romantic loneliness. So, one of the word groups that are grouped by assonance (here: "ei") affects the meaning of the other group (here "a").

"""
```

```python
printmd(gemini(prompt_transfer))
```

```python
%%ai gpt4o
{prompt_transfer}
```

```python
%%ai opus
{prompt_transfer}
```
