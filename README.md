# llms_read_hoelderlin

Repository for notebooks used in the paper:

Jannidis, Fotis/Kleymann, Rabea/Schröter, Julian/Zinsmeister, Heike: "Do Large Language Models understand literature? Case studies and probing experiments on German poetry." *Journal of Computational Literary Studies* 2025

A previous version for the *Conference of Computational Literary Studies* 2025 was published here: https://tuprints.ulb.tu-darmstadt.de/entities/publication/1da102a8-2f12-4f0c-8294-37f8c52b6945
DOI: 10.26083/tuprints-00030139 


## Installation of dependencies
`pip install -r requirements.txt`
You also need api keys from OpenAI, Anthropic and Google to replicate the research!

## The structure of the repository

The probing experiments in this paper have four levels of order. 

### I) Interpretive Tasks

For the first dimension, we divide the experiments into nine different types of interpretation tasks, each of which corresponds to a Jupyter notebook (NB) in this repository. These tasks include:

`01_metrics.ipynb`

`02_rhyme.ipynb`

`03_assonances.ipynb`

`04_lexis.ipynb`

`05_phrases.ipynb`

`06_syntax_vers.ipynb`

`07_metaphors.ipynb`

`08_titles.ipynb`

`09_textmeaning.ipynb`

### II) Poems
Each task is then, on the second dimension, performed for two poems, individually. 
We are using two texts for our analyses. One is a very well-known poem, 'Hälfte des Lebens' ('The middle of life') by Friedrich Hölderlin, a very famous German poet from the early 19th Century. There are many representations of this poems in German and English online and also many interpretations. 
The other poem, 'Unsere Toten', by Hans Pfeifer, is unknown to Google at the time of writing and has not been published again after its first publication 1922. The author is also not a known figure in literary history. 

#### Friedrich Höderlin: Hälfte des Lebens (1804)

Mit gelben Birnen hänget 

Und voll mit wilden Rosen 

Das Land in den See, 

Ihr holden Schwäne, 

Und trunken von Küssen 

Tunkt ihr das Haupt 

Ins heilignüchterne Wasser.

--

Weh mir, wo nehm’ ich, wenn 

Es Winter ist, die Blumen, und wo 

Den Sonnenschein, 

Und Schatten der Erde? 

Die Mauern stehn 

sprachlos und kalt, im Winde 

klirren die Fahnen.

--

First published in 1804 in Friedrich Wilman's "Taschenbuch für das Jahr 1805"

In: Friedrich Hölderling: Gesammelte Werke. Herausgegeben von Hans Jürgen Balmes. Frankfurt am Main: Fischer, p. 163.

[![Hälfte_des_Lebens.png]](https://github.com/cophi-wue/llms_read_hoelderlin/blob/05cc5a7c1e89fa9056149be40f8793a480ee3d92/images/H%C3%A4lfte_des_Lebens.jpg)

#### Hans Pfeifer: Unsere Toten (1922)

Von Westen und Osten, von Nord und Süd

Schleppen sich nächtens viele Füße müd,

Füße, vom Wandern wund und zerfetzt,

Langsam bedächtig zur Erde gesetzt,

Müh'n sich im zitternden Mondenschein

Rastlos tief nach Deutschland hinein.

Und wer mit lauschendem Ohr noch wacht

Hört sie in jedweder werdenden Nacht,

Hört dies Schlurfen so müde und schwer,

Hört eine Klage voll wilder Begehr,

Eine Klage schmerzzerfressen:

Nur nicht vergessen! Uns nicht vergessen!


In: Uhlmann-Bixterheide, Wilhelm, ed. (1922). Die deutsche Balladen-Chronik. Ein Balladenbuch von deutscher Geschichte und deutscher Art. Dortmund: Ruhfus, p. 290. 

The texts and several translations into English can be found in the `definitions.py`.

[![Unsere_Toten.png]](https://github.com/cophi-wue/llms_read_hoelderlin/blob/0fbcee33dbc845bf5590896791dac7c52335f10e/figures/Unsere_Toten.png)

#### III) Levels of Complexity
Regarding the third dimension of For each of these nine tasks, we distinguish three levels of complexity of the tasks: 
1. General knowledge (corresponds to chapter 3 in the paper)
2. Expert knowledge (corresponds to chapter 4 in the paper)
3. Abstraction and Transfer (corresponds to chapter 5 in the paper)

Specific prompts were developed for each level of complexity. The individual prompts can therefore be viewed at this level. The paper is structured into chapters corresponding to these three levels of complexity. In order to make our argumentation in the paper as concise as possible, the important results for each of the nine tasks (level I) are discussed together within the chapters on the three levels of complexity.

### IV) Models
The LLMs being used and tested are:
1. OpenAi: ChatGPT-4o (gpt-4o-2024-08-06)
2. Anthropic Claude 3.5 Sonnet 2024-10-22
3. Google Gemini 1.5 Pro (Sep 2024)

After some pre-studies we decided not to use open source models like Llama 3.1:70b, because they didn't perform as well as the commercial models offered by OpenAI, Google and Anthropic. Llama 3.1:405b wasn't an option because we didn't have access to an infrastructure able to run it. 
Our selection was based on evaluations of these models on Chatbot Arena (1.11.2024): https://lmarena.ai/ 

[![model_comparison.png]](https://github.com/cophi-wue/llms_read_hoelderlin/blob/05cc5a7c1e89fa9056149be40f8793a480ee3d92/images/model_comparison.png)

The notebooks therefore each have the following identical structure: 

## The Structure of all Jupyter Notebooks

### 1 The interpretive Task:
A notebook is dedicated to each interpretation task (I). The first Notebook is on "metrics (`01_metrics.ipynb`), the secon on rhyme (`02_rhyme.ipynb`), etc.

Each notebook starts with a code block on Configuration: Here, the LLMs are loaded and the parameter space is set.

### 1.1 Poem (1) Hölderlin: *Hälfte des Lebens*

#### 1.1.1 Level of complexity (1) General Knowledge: 

- Prompt 1.1.1 (or a series of prompts) taylored to the respective task, level of complexity, and poem)

- Execution of the prompt(s) for all LLMs examined 
    ##### 1.1.1.1 ChatGPT
    ##### 1.1.1.2 Anthropic Claude
    ##### 1.1.1.3 Google Gemini

#### Level of complexity (2) General Knowledge

- Prompt 1.1.2 (or a series of prompts) taylored to the respective task, level of complexity, and poem)

- Execution of the prompt(s) for all LLMs examined 

#### Level 3) Abstraction and Transfer

- Prompt 1.1.3 (or a series of prompts) taylored to the respective task, level of complexity, and poem)

- Execution of the prompt(s) for all LLMs examined 

### Poem 2) Pfeiffer: *Unsere Toten*

#### Level 1) General Knowledge: 

Prompt 1.2.1 (or a series of prompts) taylored to the respective task, level of complexity, and poem)

Execution of the prompt(s) for all LLMs examined 

#### Level 2) General Knowledge

Prompt 1.2.2 (or a series of prompts) taylored to the respective task, level of complexity, and poem)

Execution of the prompt(s) for all LLMs examined 

#### Level 3) Abstraction and Transfer

Prompt 01.2.3 (or a series of prompts) taylored to the respective task, level of complexity, and poem)

Execution of the prompt(s) for all LLMs examined 


In this way, the same structure is continued in all notebooks on the nine interpretation tasks.

## Further files
- `all_tasks.ipynb`: A Jupyter Notebook (NB) merging all 9 NBs on the interpretive tasks omitting the LLMs' output.
- `definitions.py`: The German as well as English versions of both poems wrapped with a Text class and methods that allow to import the texts and their translations into the jupyter notebooks.
- `requirements.txt`: Dependencies and Requirements for the virtual environment. Among others, the Jupyter AI Magics and Langchain modules are
- `utils.py`: Classes and functions for configuring and implementing access to the LLMs being used (through the LangChain modules). Here, the models are specified and the path to your personal API keys is defined.
- `LICENCSE`
- You will have to add in your local copy of the repository the following files: `key_openai.txt`, `key_google.txt`, `key_anthropic.txt` including your personal API keys.
- Note that for the NB `09_textmeaning.ipynb`we refer to a poem that is under copy-right and that needs to be opened separately. For private use, you can ask us for the respective file `Ǹovak_Haeuser.txt` that needs to be stored in your local copy of this repository.


