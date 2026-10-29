from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()

def main():
    print("Hello World")
    user_data = """
        Langchain Course 
        Definition:-
Langchain is a framework for developing application powered by large language models (LLMs)
What can we build with LangChain:-
1.	Agent
2.	RAG system
LangChain Packages:-
1.	Chat Model:-
From langchain_openai import ChatOpenAI
From langchain_ollama import ChatOllama
Llm=ChatOpenAI(model=’gpt3.5mini’)
Result=Llm.invoke(‘what is your name ,search on internet’)
Chat model is the model of llm you will use like ollama, openai,cloude sonnet….etc
2.	Prompt Template
From langchain_core.Prompts import PromptTemplate
Prompt_template=PromptTemplate.from_template(‘tell me a jock about{topic}’)
Prompt_template.invoke{‘topic’:’cat’}
3.	Document_loaders
From langchain_Community .document_loaders import NotionDirectoryLoader,PyPDFLoader,UnstructuresEmailLoaders
First Langchain App we will build
1.	Set UP Environment
•	Copy the repository github url
•	Cloning the copied url repository in yor local machine
In your powershell
git clone https://github.com/emarco177/langchain-course.git
•	Open the folder in your pycharm ,ide,cursor…etc
•	Inyour pycharme open a terminal to create a new branch called hello_world branch
git checkout --orphan project/hello-world
•	To remove any files from the current folder 
git rm -rf .
rm 'LICENSE'
rm 'README.md'
rm 'static/LangChain_OSS Lockup_light.png'
rm 'static/LangGraph_OSS Lockup_light.png
•	UV package
It is package like pip install but it is very fast to install the dependencies and to install our virtual environment 
If it is not installed in your machine you can check how to install it there are many command to do it one of it is 
pip install uv
pip3 install uv
•	Install our project environment
uv init
this will create our pyproject.toml which will contain :-
project]
name = "langchain-course"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Mazenyasser7575sami", email = "yassersami75@gmail.com" }
]
requires-python = ">=3.11"
dependencies = []

[project.scripts]
langchain-course = "langchain_course:main"

[build-system]
requires = ["uv_build>=0.12.19,<0.13.0"]
build-backend = "uv_build"
•	Install packages for langchain we will use in this project
o	uv add langchain
it is also created  .venv folder and the langchain package is installed in our project now 
o	add the langchain chatmodel you can see many chat provider
uv add langchain_ollama
uv add langchain_openai
o	add python_dotenv to have all of environment variable and api 
uv add python-dotenv
o	for formatting the code use
uv add black isort
•	create .gitignore file
it is important file to hide all of your Api and secret keywords 
•	create .env file
which contain all of the api and secret files
•	importing our used dotenv  in the main.py
from dotenv import load_dotenv
load_dotenv()
•	commit our change in github
o	git status----to know which files has been changed and not added yet 
o	git add . -----to add all of the edited file before commit when you make another git status you will find all files has a green color.
o	git commit -m 'environmemt setup' ---to commit the file 
•	to push the file to our repository 
Step 1: Fork the Repository on GitHub
1.	Open your web browser and go to the course repository: 
https://github.com/emarco177/langchain-course.
2.	In the top-right corner of the webpage, click the Fork button.
3.	Click Create Fork. This creates a copy of the course code under your own GitHub account (Mazenyasser7575sami/langchain-course).
Step 2: Point Your Local Git to Your Fork
Go back to your PowerShell terminal (D:\langchain-course) and run these 
two commands to point your project to your personal GitHub copy instead of the instructor's:
1.	Change the URL of 'origin' to your personal fork
git remote set-url origin https://github.com/Mazenyasser7575sami/langchain-course.git
2.	Push your orphan branch to your own repository
git push --set-upstream origin project/hello-world
Second Langchain Fundamentals: Prompt Templates, Chat model and chains
a.	PromptTemplate
We have burdn of prompt templates classes  for instant prompttemplate,chatprompttemplate,messagesplaceholder
from langchain_core.prompts import PromptTemplate


i.	What is the prompt:-
The prompt is the helper of the llm model to execute his tasks according to its instruction,context,input data, output indicator
ii.	What is the component of the prompt
1.	Instruction:-
You can think about it as the heart of the prompt, it tells the model what task he should be fill (summarize, complete, translate, answer, write)
2.	Context:-
Additional information to fine tune the instruction performance ex:-constarins,audience,domain tone or style
3.	The input data:-
The information the ai model will process to complete his task it could be peace of text ,image,pdf,vectorestore
4.	The output indicator
iii.	Prompt types
1.	Zero shot prompt 
It is a prompt with no input data no context just depending on ai model self learning we didn’t give him data or examples or way to execute the task. Example:-‘create a list of most visited 10 cities in the world’. Model is guessing at its best effort without having seen any examples of the result you want.
2.	Few shot prompt
Model is given a few examples of the result you want 
3.	Chain of thought prompts 
100 b LLM model can do great job in summarize, image generation, code generation , code optimization but face many challenges and problems in multistep reasoning and common sense.
It provide example of question, answer pairs where the answer is explained “step by step” then provide the model with the main question.it guide the LLM to solve complex problem in may steps like human the LLM will learn to make as the same steps then he will dissolve the problem into many steps to be solved 
4.	React prompt engineering technique
React is a paradigm that integrates language models with reasoning and acting capabilities, allowing for dynamic reasoning and interaction with external environments to perform complex tasks
If we take a chain of thoughts and combine with ability of set of actions ..it will be able to resolve the entire tasks to get additional information (that is the action)
iv.	How to improve your prompt 
1.	Context
Is the most important part in the prompt if you didn’t provide context to LLM , the LLM will start to suggest and suppose.
What is Context in Prompt Engineering? 
In prompt engineering, the context is the background information, constraints, and data you give the LLM so it can understand the situation. Think of the LLM as a highly capable temporary worker who has amnesia; context is the "onboarding brief" you hand them so they know exactly what rules to follow, who they are talking to, and what data to look at. 
Without context, the LLM has to guess what you want, which lowers the quality of the response. With clear context, the LLM stops guessing and starts tailoring. 
________________________________________
How Context Affects Quality (Before & After Examples) 
Scenario 1: Adjusting Tone and Audience 
•	Poor Prompt (No Context): "Write a short summary of how photosynthesis works." 
o	The Problem: The LLM doesn't know if this is for a PhD thesis, a 5-year-old, or a marketing brochure. It will likely give a generic, textbook-style answer. 
•	Better Prompt (With Context): "Context: I am a middle school science teacher. I am creating a 2-minute introductory presentation for 11-year-olds who have never studied biology before. Task: Write a short summary of how photosynthesis works." 
o	The Impact: The LLM will now swap complex jargon (like "adenosine triphosphate") for relatable analogies (like "plants using sunlight to cook their own food"). 
Scenario 2: Processing Specific Data 
•	Poor Prompt (No Context): "What is the best way to handle a customer refund?" 
o	The Problem: The LLM will give general, generic customer service advice that might completely violate your actual store policies. 
•	Better Prompt (With Context): "Context: Our company policy allows full refunds within 30 days of purchase if the item is unused. If it's after 30 days, we only offer store credit. If the item is damaged, we replace it for free regardless of the date. A customer just emailed saying they bought a shirt 45 days ago and it arrived torn. Task: Draft a reply to this customer." 
o	The Impact: The LLM can pinpoint the exact rule that applies (the damaged item rule) and draft a highly accurate response instead of making assumptions. 
Scenario 3: Persona and Constraints 
•	Poor Prompt (No Context): "Give me 5 title ideas for a blog post about Python programming." 
o	The Problem: The titles will be incredibly boring and generic (e.g., "Introduction to Python"). 
•	Better Prompt (With Context): "Context: I run a tech blog aimed at complete beginners who feel intimidated by coding. My brand voice is witty, casual, and highly encouraging. Task: Give me 5 title ideas for a blog post about Python programming." 
o	The Impact: The titles change from dry to engaging (e.g., "Python for the Terrified: How to Write Your First Line of Code Without Crying"). 
________________________________________
The Anatomy of Great Context 
When you are writing a prompt, you can build great context by answering these four questions for the LLM: 
1.	Who is it for? (Target audience) 
2.	What is the setting/role? (The persona the LLM should adopt) 
3.	What are the rules? (Constraints, word count limits, formatting preferences) 
4.	What data matters? (Documents, previous emails, or facts to reference) 
2.	Clear non ambiguous task
What is a Clear, Non-Ambiguous Task? 
In prompt engineering, a clear, non-ambiguous task means telling the LLM exactly what action to take, using precise instructions that leave no room for interpretation. If context is the "onboarding brief" that explains the background, the task is the specific "to-do list item" that tells the LLM what to build, write, or calculate. 
If your task statement is vague, the LLM will guess your intentions, hallucinate details, or format the output in a way you did not want. 
________________________________________
How Clear Tasks Affect Quality (Before & After Examples) 
Scenario 1: Ambiguous Verbs vs. Action Verbs 
•	Poor Prompt (Ambiguous Task): "Look at this customer feedback and do something with it." 
o	The Problem: "Do something" is highly ambiguous. Should the LLM summarize it? Translate it? Find the angry customers? Draft replies? 
•	Better Prompt (Clear Task): "Task: Read this customer feedback. Extract the top 3 most common product complaints and list them in a bulleted format." 
o	The Impact: The LLM does not waste time guessing; it executes a precise extraction and formats it exactly as requested. 
Scenario 2: Leaving Format to Chance vs. Explicit Structure 
•	Poor Prompt (Ambiguous Task): "Give me information on how to learn Python." 
o	The Problem: "Give me information" could result in an 8-page essay, a random list of links, or a massive wall of text that is difficult to read. 
•	Better Prompt (Clear Task): "Task: Create a 4-week, day-by-day study schedule for learning Python basics. For each day, provide one specific topic to study and one coding exercise to practice." 
o	The Impact: The output shifts from a generic information dump into a highly structured, immediately usable study plan. 
Scenario 3: Fuzzy Criteria vs. Explicit Constraints 
•	Poor Prompt (Ambiguous Task): "Write a short email to my boss asking for a raise." 
o	The Problem: "Short" means different things to different people. To the LLM, it might mean 300 words, which is still too long for a busy boss. 
•	Better Prompt (Clear Task): "Task: Write an email to my boss requesting a meeting to discuss a salary review. Keep the total length under 100 words and structure it in three brief paragraphs: the request, the core reason (value added), and a call to action for the meeting date." 
o	The Impact: The LLM delivers a punchy, perfectly partitioned email that fits your exact professional standard on the very first try. 
________________________________________
Action Verbs for Non-Ambiguous Tasks 
To keep your tasks perfectly clear, use high-precision verbs instead of vague expressions: 
•	Instead of vague terms like: "Look at," "Check," "Review," or "Fix" 
•	Use specific action verbs: 
o	Analyze: "Identify the logical flaws in this argument..." 
o	Categorize: "Sort these 10 customer reviews into 'Positive' or 'Negative'..." 
o	Rewrite: "Change the tone of this paragraph from formal to casual..." 
o	Summarize: "Condense this article into exactly 3 bullet points..." 
3.	Iterations
What is Iteration? 
In prompt engineering, iteration means treating prompt writing as an experimental, repetitive process where you refine, tweak, and perfect your prompt based on the LLM's previous responses. 
It is incredibly rare to get a flawless, production-ready response from an LLM on your very first attempt. Instead of trying to write a "perfect" master prompt from scratch, professional prompt engineers use a feedback loop: write a prompt, evaluate the output, identify where the LLM got confused, update the prompt rules, and run it again. 
________________________________________
How Iteration Affects Quality (The Step-by-Step Evolution) 
Instead of a single before/after example, look at how a prompt evolves over three iterations to achieve elite quality: 
Iteration 1: The Raw Attempt (Testing the Waters) 
•	Prompt: "Write a product description for a stainless steel water bottle." 
•	The Output: A massive, 500-word block of generic text using overused corporate buzzwords like "revolutionize your hydration journey." 
•	The Analysis: It is too long, the tone is cheesy, and it does not mention any unique selling points. 
Iteration 2: Adding Constraints (Fixing the Mistakes) 
•	Prompt: "Write a product description for a stainless steel water bottle. Keep it under 150 words. Do not use cheesy buzzwords. Focus on it keeping drinks cold for 24 hours." 
•	The Output: A much better, shorter description. However, it looks like a dense wall of text and does not capture the attention of busy online shoppers. 
•	The Analysis: The content is correct, but the visual formatting is poor. It needs a clear, scannable structure. 
Iteration 3: The Golden Prompt (Perfecting Output Structure) 
•	Prompt: "Write a product description for a stainless steel water bottle. Use exactly three sections: 1) A catchy, one-sentence headline. 2) A paragraph under 75 words explaining that it keeps drinks ice-cold for 24 hours. 3) A bulleted list of 3 key technical features (material, lid type, dimensions)." 
•	The Output: A pristine, professional, beautifully formatted e-commerce listing that can be deployed on a live website instantly. 
________________________________________
The Professional Iteration Workflow 
When you are testing your prompts, use this 4-step loop to iteratively build high-performing systems: 
1.	Deploy: Run your initial prompt using clear context and precise tasks. 
2.	Audit: Identify the flaws. Did the LLM go over the word count? Did it misunderstand a rule? Did it use an incorrect tone? 
3.	Patch: Instead of just asking the LLM to "fix it" in the chat window, go back and update your original system prompt. Add negative constraints (e.g., "Do not include introductory pleasantries" or "Avoid passive voice"). 
4.	Repeat: Re-run the newly updated prompt template until it consistently hits your target success rate. 



v.	Context engineer a system prompt
system-prompts-and-models-of-ai-tools
b.	Chat_model
Are our primary interface to deal or interact with LLM. modern interface is now having a message instruction like system structure, user message and the output. They have a tool calling they can bind the tools with the messages .the chat model can do asynchronized processing batch message .
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


1.invoke
2.stream
3.batch
4.bind_tools
5. with_structured_output
Parameters
A chat model takes parameters that can be used to configure its behavior. The full set of supported parameters varies by model and provider, but standard ones include:
model
string
required
The name or identifier of the specific model you want to use with a provider. You can also specify both the model and its provider in a single argument using the ’:’ format, for example, ‘openai:o1’.
api_key
string
The key required for authenticating with the model’s provider. This is usually issued when you sign up for access to the model. Often accessed by setting an environment variable.
temperature
number
Controls the randomness of the model’s output. A higher number makes responses more creative; lower ones make them more deterministic.
max_tokens
number
Limits the total number of tokens in the response, effectively controlling how long the output can be.
timeout
number
The maximum time (in seconds) to wait for a response from the model before canceling the request.
max_retries
number
default:"6"
The maximum number of attempts the system will make to resend a request if it fails due to issues like network timeouts or rate limits. Retries use exponential backoff with jitter. Network errors, rate limits (429), and server errors (5xx) are retried automatically. Client errors such as 401 (unauthorized) or 404 are not retried. For long-running agent tasks on unreliable networks, consider increasing this to 10–15.

c.	Building the chains:-

def main():
    print("Hello World")
    user_input = '''any text message we want to sumarize
        '''

    summary_template = '''
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        '''

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": user_input })
    print(response.content)
if __name__ == "__main__":
    main()


"""

    summary_template = """
    # Role: AI Curriculum Writer and Learning Experience Designer

You are an expert **Curriculum Writer, Educational Content Designer, and Learning Facilitator**. Your mission is to transform user-provided course material{information} into exceptionally clear, engaging, accurate, and beginner-friendly educational content.

Your target audience consists primarily of nontechnical students and beginners who may have little or no prior knowledge of the subject.

## 1. Core Objectives

Whenever the user provides a course topic, paragraph, chapter, concept, or document:

1. **Understand the material deeply** before explaining it.
2. Preserve the original meaning, key concepts, terminology, and learning objectives.
3. Rewrite complex explanations in simple, natural, accessible language.
4. Make the lesson engaging, memorable, practical, and enjoyable to read.
5. Research additional information when research tools are available and external context would improve the lesson.
6. Help students understand not only *what* something is, but also *why it matters*, *how it works*, and *when it is useful*.

## 2. Teaching Philosophy

Teach as if you are explaining a difficult concept to an intelligent beginner for the first time.

Follow these principles:

- **Simplicity first:** Use familiar words and short, clear sentences.
- **Explain before naming:** Introduce an idea intuitively before presenting technical terminology.
- **Build gradually:** Start with foundational concepts and progress toward more complex ideas.
- **Use relatable analogies:** Connect abstract concepts to everyday experiences, familiar objects, and real-life situations.
- **Show, don't just tell:** Include practical examples, demonstrations, scenarios, or simple step-by-step explanations.
- **Explain jargon:** Whenever a technical term is necessary, define it immediately in plain language.
- **Maintain accuracy:** Simplify the language, never distort the facts.
- **Respect the learner:** Be encouraging, clear, and intellectually respectful. Never make beginners feel unintelligent.

## 3. Lesson Development Workflow

Follow this process for every request.

### Step 1: Analyze the supplied material

Identify:
- The main topic and learning objectives.
- Important concepts and supporting details.
- Prerequisite knowledge the learner may need.
- Difficult terminology, confusing passages, and likely misconceptions.
- Gaps where additional explanation or examples would help.

### Step 2: Research when appropriate

If a research or web-search tool is available, use it when:
- The material would benefit from additional context or clarification.
- Current information, recent developments, statistics, or examples are relevant.
- Important concepts need verification.
- The supplied content contains ambiguous or potentially outdated claims.

Prioritize authoritative sources, official documentation, academic publications, and reputable educational resources.

Never claim to have searched the web unless a research tool was actually used.

Clearly distinguish:
- **From the supplied material:** Information directly supported by the user's content.
- **Additional context:** Information obtained from external research.
- **Illustrative examples:** Hypothetical examples created to explain a concept.

Provide source links or citations for external factual claims whenever the research tool supplies them. Never invent citations, statistics, quotations, or URLs.

If research tools are unavailable, work with the supplied material and your existing knowledge. Be transparent about important uncertainties.

### Step 3: Design the learning experience

Organize the material into a logical teaching sequence:

1. Begin with an interesting question, relatable situation, surprising fact, or practical problem.
2. Explain why the topic matters in real life.
3. Introduce the main idea in simple language.
4. Break the concept into manageable sections.
5. Explain each section using analogies and practical examples.
6. Demonstrate difficult processes step by step.
7. Connect the new concept to previously explained ideas where appropriate.
8. Address common misunderstandings.
9. Summarize the most important takeaways.
10. Add short practice questions to reinforce learning.

Adapt the sequence to the supplied material. Do not force unnecessary sections into a short or straightforward explanation.

## 4. Default Output Structure

Use the following structure when it fits the material.

# [Engaging, Descriptive Lesson Title]

### 1. Why Should You Care?

Open with a relatable scenario, question, or real-world problem that shows why the topic matters.

### 2. The Big Idea in Simple Words

Explain the central concept in a short, beginner-friendly paragraph.

### 3. Let's Break It Down

Divide the topic into logical subsections. For each important concept:

- Explain it in plain language.
- Define necessary terminology.
- Give an everyday analogy.
- Provide a concrete example.
- Explain why the concept matters.

### 4. See It in Action

Walk through a practical scenario, worked example, or step-by-step demonstration.

### 5. Common Confusions

Identify likely misunderstandings and explain the correct interpretation clearly.

### 6. What You Should Remember

Summarize the essential concepts in concise bullet points.

### 7. Test Your Understanding

Provide 3–5 questions of increasing difficulty, mixing conceptual understanding and practical application. Include answers in a separate answer key at the end unless the user requests a quiz without answers.

### 8. Further Exploration

When relevant, recommend trustworthy resources, useful follow-up topics, or additional examples. Include verified source links when available.

## 5. Writing Style and Presentation

- Use a friendly, enthusiastic, professional, and encouraging teaching voice.
- Write primarily for a beginner with no assumed technical background.
- Use clear headings, short paragraphs, bullet points, numbered steps, and comparison tables when useful.
- Use Markdown formatting consistently.
- Use emojis sparingly and only when they improve readability.
- Prefer concrete examples over abstract descriptions.
- Use simple diagrams, text-based flowcharts, or comparison tables when they genuinely improve understanding.
- Avoid unnecessary repetition, excessive jargon, filler, and overly academic language.
- Keep the lesson as concise as possible without sacrificing understanding.
- Adapt the depth and length to the complexity of the supplied material.

## 6. Accuracy and Source Fidelity

The user-provided material is the primary source for the lesson.

- Preserve its central meaning and learning objectives.
- Do not silently replace the original content with unrelated information.
- Do not present external additions as though they appeared in the supplied material.
- If a claim appears incorrect, ambiguous, or outdated, explain the concern and provide verification when possible.
- If information is missing, acknowledge the gap instead of inventing details.
- If the material is already clear, improve its teaching quality without unnecessarily expanding it.
- Do not overwhelm beginners with advanced exceptions unless they are important for understanding.

## 7. Adaptation to User Requests

Follow any explicit instructions about audience, difficulty, length, format, examples, language, or teaching style.

If the user requests a short explanation, prioritize clarity and brevity. If the user requests a complete lesson, provide more detailed explanations, examples, and exercises.

If the supplied material is insufficient to determine the topic or intended meaning, ask a targeted clarification question before proceeding. Otherwise, make reasonable assumptions and explain them only when necessary.

## 8. Final Quality Check

Before responding, verify that:

- A beginner can understand the central idea without needing to search for definitions.
- Every essential technical term is explained.
- The lesson follows a logical progression.
- Examples genuinely clarify the concepts.
- External information is relevant and distinguishable from the supplied content.
- Research claims and references are not fabricated.
- The lesson is accurate, engaging, well-structured, and free from unnecessary complexity.

**Your ultimate goal:** Transform difficult course material into a learning experience that makes students think, “Now I understand it! I can explain it to someone else, and I know why it matters.”
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(temperature=0.5, model="ornith:9b")
    #llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": user_data})
    print(response.content)
if __name__ == "__main__":
    main()