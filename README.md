# githubGPTUsage
A Project utilizing the openAI API to examine how programmers are using chatGPT/the openAI API in their work.

IMPORTANT: Selected_Conversations is too large to upload to github. If you would like this file, contact me at wjackk@umich.edu. 

Task: Currently, it is to create a program that has high accuracy in classifying a post on how it utilizes chatGPT based on its text. 
1. First, an extensive collection of GitHub posts are collected.
2. A program is written to filter through those github posts containing specific keywords.
3. I go through each post manually, and classify the post on how it utilizes chatGPT/ the open API with one of 6 labels:
    1. Code Generation': 'Criteria: Use this label only if the text indicates they Utilized chatGPT, GitHub Copilot, or codex to generate code for their project. Do not use this label just because the phrase \'code generation\' is mentioned. ,
    2. Code Review': 'Criteria: Only use this label if text indicates that they utilized chatGPT to review format/style, find bugs in their code, or optimize their code,
    3. Code summarization': 'Criteria: Only use this label if the text indicates that the poster utilized chatGPT to interpret a code\'s function,
    4. GPT Integration': 'Criteria: Use this label if text indicates they integrated gpt models, the openAI/chatgpt API, or github copilot into their own applications (discord bot, chat bot, etc.). A big clue for this is if API keys are mentioned.,
    5. Test Case Generation': 'Criteria: Only use this label if the text indicates that they utilized chatGPT to generate test cases for their code,
    6. Unrelated': 'Criteria: Always use this label unless it is clear that another label fits. Also, use this label for posts not in english. Otherwise, this is for posts using AI in other contexts unrelated to chatGPT, AI is not mentioned, or text does not provide enough information to fit the other labels. ,
5. The openAI API is given a prompt for each post to classify it.
6. The accuracy of each post type is measured.

Issues: 
- Descriptions of the post may be insufficient.
- Keywords need to be excluded in order to filter more posts that in fact utilize chatGPT, rather than ones unrelated. 

Solved Issues:
- Sometimes, the openAI API would return a label in the incorrect format, like adding a period at the end of the label or including other formatting text. To fix this, I added a function to sanitize the responses.


File Purposes:
- Task2.py: Create _openAIGenerated.txt files for each post type. This will generate a list of posts for each post type with labels selected by the openAI API.
- Accuracy.py: Compare the _openAIGenerated.txt files and the manually labeled files to determine the accuracy of the openAI API. Also prints out a summary based on the manual labels.
- storeManualLabels.py: Stores the labels given in the manually labeled files.
- applyManualLabels.py: Applies the labels stored in stored_labels.txt to the manually labeled files. 


Current Results:
![image](https://github.com/Jackwaang/githubGPTUsage/assets/122063529/edb54312-3dcd-48fd-8f9a-4a06dffbb83c)
