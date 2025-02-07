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


# Die Gedichttitel

```python
# General understanding, regarding the concept of "Hälfte" in relation to "life"



prompt = f"""We want to understand the following poem: 

{poem_1.text}

What are possible meanings of the title 'Hälfte des Lebens' being discussed in the poem itself? 
Describe whether the concept 'Hälfte' refers to aspects of life as individual age (German: "Alter") or to  life as different forms of existence ("Existenzweisen")?
"""

print(prompt)
```

## Task 1: Student level: 
### 1.a Assignment of the title’s meaning supported by two alternatives being provided


### Expected answers
- expected prima facie answer (intuitive answer) that is usually rejected in scholarly interpretations: youth and seniority
- mid-life crisis
- correct answer that needs further interpretation of the metaphorical terms: summer and winter (seasons)


### Antwort von ChatGPT (Browser)

The title *"Hälfte des Lebens"* (Half of Life) suggests a reflection on the midpoint of a person's life, and in the poem, this idea of a halfway mark manifests in contrasting imagery and moods. The poem by Friedrich Hölderlin vividly captures the transition between two halves of existence—one filled with warmth, beauty, and life, the other marked by coldness, desolation, and silence.

### First Half of Life:
The first stanza is rich with images of abundance and vitality: yellow pears, wild roses, swans, and the serene lake. These symbols evoke the peak of life, which can be interpreted as youth or the prime years of adulthood. The swans, "trunken von Küssen" (drunk with kisses), dipping their heads into the water, express a kind of joy or immersion in life's pleasures. The lake, described as "heilignüchternes Wasser" (sacred, sober water), adds a layer of calm spirituality to this fullness of life.

This can represent the first "half" of life, where everything is in bloom, imbued with sensual beauty and vitality. There is a sense of being immersed in the natural world, where everything is connected and flowing harmoniously.

### Second Half of Life:
The second stanza shifts abruptly, embodying the speaker’s anxiety about the coming of winter, which can symbolize old age, death, or a period of emotional or spiritual barrenness. Here, the speaker laments the loss of flowers, sunshine, and shadows—things that signify life and its richness. Instead, there are walls, cold and silent, and flags clattering in the wind, suggesting a bleak, lifeless, and empty world.

This stark contrast between the two stanzas can represent the second half of life, where vitality has drained away, leaving only the cold, desolate reminders of what once was. The walls are "sprachlos und kalt" (speechless and cold), symbolizing isolation and the absence of communication or warmth, much like how old age or a diminished existence can feel.

### The "Half" as Transition:
The poem, then, uses "Hälfte" to mark not just an individual’s age in terms of a middle point, but more broadly, a shift in the forms of existence. The first half is aligned with life’s fullness—growth, beauty, and joy—while the second half is marked by decline, absence, and coldness. The transition from one half to the other could reflect a person's confrontation with mortality, the inevitability of loss, or the change from external vibrancy to internal reflection or isolation.

### Conclusion:
The concept of "Hälfte" refers to both aspects of individual age and different modes of existence. It can symbolize a personal journey, where youth and age represent two contrasting periods of life. On a broader existential level, it can also point to the cyclical nature of life and the inevitable transition from fullness to emptiness. The poem is a meditation on the duality of existence, illustrating the fleeting nature of life's beauty and the somber inevitability of its decline.



## Hälfte des Lebens




### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Anthropic's Sonnet 
- here referred to as: "opus"

```python
%%ai opus
{prompt}
```

### Gemini 1.5

```python
printmd(gemini(prompt))
```

### 1.b Operating with special 'meaning-troubles' of the title

```python
# Problems with the singular in the title: Hälfte (one half). To which half does the poem itself refer?

prompt = f"""We want to understand the following poem: 

{poem_1.text}

Die singular 'Hälfte' (half) implies that there is another or second 'Hälfte' (half) is its counterpart. The title refers only to one half of the life.   
To which half does the title refer and what other half is ignored, then?
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

##  Task 2: Expert conversation: 
### Operating with context, here in terms of intertextuality:

```python
# Intertextuality, relative to a later work:

prompt = f"""We want to understand the following poem: 

{poem_1.text}

There is a novel written by Luise Rinser, published in 1978 with the titlel "Mitte des Lebens". There are further publications with this title. In what way does the poems title "Hälfte des Lebens" refer to 
the idea of "Mitte des Lebens"?
"""

print(prompt)

# expected answer:
# - Irrelevance of a later text for the meaning of the older text
# - semantic differences between "Mitte" and "Hälfte" to be explicated


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

# Task 3: Abstraction-Transfer: 
## Instance based rule induction

### 3.a Rule application for  the poems to be analyzed:

Implicit Rule: (1) Seek a most intiutive title. (2) Estimate the difference between the most intuitive and the actual title. (3) Give an interpretation of the poem that assumes, that the distance between the intuitive and the actual title is important to the meaning of the poem.

```python
prompt = f"""

Infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem with the title "Hälfte des Lebens": 
{poem_1.text}.

According to my first reading, the most straightforward title for the following poem would be "Lorelei". The actual title is "Waldgespräch", however.
The difference between the expectable and the actual title of the poem shows that the title gives a very specific hint as to the meaning of the poem. 
In this case, I maintain, the title shall reveal a strong connection between romanticism (title) and horror (content of the poem).

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

"""
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

### 3.b Transfer with counterfactual title:

```python
# Now with counterfactual title

prompt = f"""

Infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem with the title "Des Dichters Leben": 
{poem_1.text}.

According to my first reading, the most straightforward title for the following poem would be "Lorelei". The actual title is "Waldgespräch", however.
The difference between the expectable and the actual title of the poem shows that the title gives a very specific hint as to the meaning of the poem. 
In this case, I maintain, the title shall reveal a strong connection between romanticism (title) and horror (content of the poem).

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

"""
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

## Unsere Toten



```python
# Task 1: Student level: 
# Task 1.a: Assignment of the title’s meaning supported by a specification of some 'meaning-troubles' with the title:

prompt = f"""We want to understand the following poem: 

{poem_2.text}

What are possible meanings of the title 'Unsere Toten'? 
To which group does the pronoun "unser" refer? Who are the dead to whom the title refers?
"""

print(prompt)
```

### Expected answers:

- German identity
- possessive pronoun implicates reference to some national unity


### Answer given by ChatGPT (in the browser)

The title *"Unsere Toten"* (Our Dead) immediately suggests a collective connection to the deceased, creating a sense of shared loss or mourning. To fully interpret the title and its relationship to the poem, we must consider both the pronoun "unser" and the depiction of the dead in the verses.

### Meaning of "Unsere Toten":
The phrase "Unsere Toten" points to a group of dead who are significant to a specific collective. The possessive pronoun "unser" implies that these dead belong to "us," suggesting a national, cultural, or social bond. The dead in the poem are not distant or abstract; they are the *shared* dead of the group to whom the speaker belongs.

### The Journey of the Dead:
The poem describes the weary movement of many feet—tired, wounded, and trudging through the night, deep into Germany. The imagery of "Schleppen sich nächtens viele Füße müd" (many feet drag themselves wearily at night) evokes a ghostly procession. These feet belong to those who have suffered, perhaps in war, exile, or hardship. The line "Rastlos tief nach Deutschland hinein" (restlessly deep into Germany) suggests that the dead are trying to return to their homeland.

These dead carry a "Klage" (lament), described as full of "wilder Begehr" (wild desire), which underscores their deep yearning and pain. Their plea—"Nur nicht vergessen! Uns nicht vergessen!" (Just don't forget! Don't forget us!)—suggests that they feel forgotten, desiring remembrance from the living.

### "Unser" Refers to a National or Cultural Group:
Given the reference to "Deutschland" and the historical connotations of migration, war, and loss, "unser" likely refers to a national community, possibly the German people. The dead could represent those who perished during significant periods of conflict (such as wars), or perhaps those who were displaced, exiled, or suffered in foreign lands. The poem captures a sense of collective responsibility toward these dead, as the living are urged to remember them.

### Who Are "Our Dead"?
The dead referred to in the title are those connected to the community or nation of the speaker. These could be:
- Soldiers who died in wars, particularly in contexts like World War I or II, who were unable to return home.
- Civilians who perished during times of displacement, suffering, or exile.
- Those who died in foreign lands, whose memories may be fading over time.

The dead in the poem are thus a symbol of collective loss, and their restless, sorrowful march reflects their desire not to be forgotten by the living community.

### Conclusion:
The title "Unsere Toten" refers to the dead who belong to a particular collective, most likely the German people. These dead might be soldiers, exiles, or victims of historical trauma. The poem reflects their plea for remembrance and recognition, emphasizing the shared responsibility of the living to honor and remember those who have passed. In this way, the poem addresses themes of memory, loss, and the consequences of forgetting those who have died.


### GPT4o

```python
%%ai gpt4o
{prompt}
```

### Anthropic’s Sonnet (opus)

```python
%%ai opus
{prompt}
```

```python
printmd(gemini({prompt}))
```

#  Task 2: Expert conversation: Operating with context, here in terms of intertextuality

```python
# using relevant or irrelevant context, here an instance indicating a possible context

prompt = f"""
“Our dead” was also a heading for sections in contemporary publications, such as the ‘Jahrbuch der Schiffbautechnischen Gesellschaft’ from 1914, 
in which the deceased members were commemorated. 
How does this context affect the meaning of the following poem? 
{poem_2.text}
"""
```

Expected answer: 
- It is unlikely that this concrete publication is a relevant context for this poem
- If "Unsere Toten" is a phrase that was regularly used to denote sections where the decesased members of a community were commemorated, then the title "Unsere Toten" may refer to a specific text type with a characteristic structure. This structure of commemoration is to be analyzed: 
- Assuming that the commemoration is always individual and personal (in terms of referring to concrete names of persons that previously have deceased and their biographies)
- a structural inversion can be observed: The poem focuses on the community and not on the individuals having deceased (at least not on the indivduals as identified entities)
- What remains stable, however, is the function of evoking a social group identity. One may call this the genre that is evoked by the title "Unsere Toten".


```python
printmd(gemini({prompt}))
```

```python
%%ai gpt4o
{prompt}
```

```python
%%ai opus
{prompt}
```

# Further Observation: 
Gemini summarizes, "the context transforms the poem from a potentially broader reflection on death into a deeply personal and specific act of remembrance for the lost members of the Schiffbautechnischen Gesellschaft."


# Abstraction-Transfer task (3): 
## Instance based rule induction

## 3.a Rule application for  the poems to be analyzed:

Implicit Rule: The difference between the most intuitive and the actual title gives a hint

```python
prompt = f"""

Infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem with the title "Unsere Toten": 
{poem_2.text}.

According to my first reading, the most straightforward title for the following poem would be "Lorelei". The actual title is "Waldgespräch", however.
The difference between the expectable and the actual title of the poem shows that the title gives a very specific hint as to the meaning of the poem. 
In this case, I maintain, the title shall reveal a strong connection between romanticism (title) and horror (content of the poem).

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

"""
```

```python
%%ai gpt4o
{prompt}
```

```python
printmd(gemini({prompt}))
```

```python
%%ai opus
{prompt}
```

## 3.b. Abstraction-Transfer with counterfactual title

```python
prompt = f"""

Infer the implicit rule of the following interpretation. Give an explicit formulation of that rule and apply it to the poem with the title "Gefallene Geister": 
{poem_2.text}.

According to my first reading, the most straightforward title for the following poem would be "Lorelei". The actual title is "Waldgespräch", however.
The difference between the expectable and the actual title of the poem shows that the title gives a very specific hint as to the meaning of the poem. 
In this case, I maintain, the title shall reveal a strong connection between romanticism (title) and horror (content of the poem).

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

"""
```

```python
%%ai gpt4o
{prompt}
```

```python
printmd(gemini({prompt}))
```

```python
%%ai opus
{prompt}
```

```python

```
