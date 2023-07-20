# githubGPTUsage
A Project utilizing the openAI API to examine how programmers are utilizing chatGPT/the openAI API in their work.

Task: Currently, it is to create a program which has high accuracy in classifying a post on how it utilizes chatGPT based on its text. 
1. First, a large collection of github posts are collected.
2. A program is written to filter through those github posts containing certain keywords.
3. I go through each post manually, and classify the post on how it utilizes chatGPT/ the openAI API with one of 6 labels: 
4. The openAPI is given a prompt for each post to classify it.
5. The accuracy of each post type is measured.

Issues: 
- Descriptions of the post may be insufficient.
- Keywords need to be excluded in order to filter more posts that in fact utilize chatGPT, rather than ones unrelated. 

Solved Issues:
- Sometimes, the openAI API would return a label in the incorrect format, like adding a period at the end of the label or including other formatting text. To fix this, I added a function to sanitize the responses.
