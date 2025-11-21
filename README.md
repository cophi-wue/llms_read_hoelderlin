# llms_read_hoelderlin

Repository for notebooks used in the paper:

Jannidis, Fotis/Kleymann, Rabea/Schröter, Julian/Zinsmeister, Heike: "Do Large Language Models understand literature? Case studies and probing experiments on German poetry." *Journal of Computational Literary Studies* 2025

A previous version for the *Conference of Computational Literary Studies* 2025 was published here: https://tuprints.ulb.tu-darmstadt.de/entities/publication/1da102a8-2f12-4f0c-8294-37f8c52b6945


## Installation of dependencies
`pip install -r requirements.txt`
You also need api keys from OpenAI, Anthropic and Google to replicate the research!

## For orientation: The structure of the repository and the system of the probing experiments

The probing experiments in this paper have four levels of order. 

### I) For the first dimension, we divide the experiments into nine different types of interpretation tasks, each of which corresponds to a Jupyter notebook (NB) in this repository. These tasks include:

`01_metrics.ipynb`

`02_rhyme.ipynb`

`03_assonances.ipynb`

`04_lexis.ipynb`

`05_phrases.ipynb`

`06_syntax_vers.ipynb`

`07_metaphors.ipynb`

`08_titles.ipynb`

`09_textmeaning.ipynb`

### II) Each task is then, on the second dimension, performed for two poems, individually (for the selection of poems, see 00_intro.ipynb.

### III) Regarding the third dimension of For each of these nine tasks, we distinguish three levels of complexity of the tasks: 
1. General knowledge (corresponds to chapter 3 in the paper)
2. Expert knowledge (corresponds to chapter 4 in the paper)
3. Abstraction and Transfer (corresponds to chapter 5 in the paper)

Specific prompts were developed for each level of complexity. The individual prompts can therefore be viewed at this level. The paper is structured into chapters corresponding to these three levels of complexity. In order to make our argumentation in the paper as concise as possible, the important results for each of the nine tasks (level I) are discussed together within the chapters on the three levels of complexity.

### IV) The LLMs being investigated (`see 00_intro.ipynb`):
1. OpenAi: ChatGPT-4o (gpt-4o-2024-08-06)
2. Anthropic Claude 3.5 Sonnet 2024-10-22
3. Google Gemini 1.5 Pro (Sep 2024)

The notebooks therefore each have the following identical structure: 

## 1 Metrics [Level of tasks and Notebooks, beginning with `01_metrics.ipynb`)

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
- `00_intro.ipynb`: Information on the LLMs being used and the poems we selected for our experiments.
- `all_tasks.ipynb`: A Jupyter Notebook (NB) merging all 9 NBs on the interpretive tasks omitting the LLMs' output.
- `all_tasks.ipynb`: A Jupyter Notebook (NB) merging all 9 NBs on the interpretive tasks omitting the LLMs' output.
- `definitions.py`: The German as well as English versions of both poems wrapped with a Text class and methods that allow to import the texts and their translations into the jupyter notebooks.
- `requirements.txt`: Dependencies and Requirements for the virtual environment. Among others, the Jupyter AI Magics and Langchain modules are
- `utils.py`: Classes and functions for configuring and implementing access to the LLMs being used (through the LangChain modules). Here, the models are specified and the path to your personal API keys is defined.
- `LICENCSE`
- You will have to add in your local copy of the repository the following files: `key_openai.txt`, `key_google.txt`, `key_anthropic.txt` including your personal API keys.
- Note that for the NB `09_textmeaning.ipynb`we refer to a poem that is under copy-right and that needs to be opened separately. For private use, you can ask us for the reps


