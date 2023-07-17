import openai
import json
import time
from datetime import datetime, timedelta

openai.api_key = 'INSERT_HERE'

keywords = ['chatGPT',
                 'OpenAI',
                 'GPT 3',
                 'gpt 3.5',
                 'gpt 4',
                 'gpt',
                 'Codex',
                 'Copilot',
                 'AI generated code'
                ]

excludedWords = ["Seems you are using me but didn't get OPENAI_API_KEY seted in Variables"]
##Make github post
##Exclude more keywords
##Make document describing project
postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']

label_choices = {
    '1. [Code Generation]': 'Criteria: Use this label only if the text indicates they Utilized chatGPT, GitHub Copilot, or codex to generate code for their project. Do not use this label just because the phrase \'code generation\' is mentioned. ',
    '2. [Code Review]': 'Criteria: Only use this label if text indicates that they utilized chatGPT to review format/style, find bugs in their code, or optimize their code',
    '3. [Code summarization]': 'Criteria: Only use this label if the text indicates that the poster utilized chatGPT to interpret a code\'s function',
    '4. [GPT Integration]': 'Criteria: Use this label if text indicates they integrated gpt models, the openAI/chatgpt API, or github copilot into their own applications (discord bot, chat bot, etc.).',
    '5. [Test Case Generation]': 'Criteria: Only use this label if the text indicates that they utilized chatGPT to generate test cases for their code',
    '6. [Unrelated]': 'Criteria: Always use this label unless it is clear that another label fits. Also, use this label for posts not in english. Otherwise, this is for posts using AI in other contexts unrelated to chatGPT, AI is not mentioned, or text does not provide enough information to fit the other labels. ',
}

def contains_chinese(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False




for wantedPostType in postTypes:
    numOfType = 0
    output_file = wantedPostType + '_openaiGenerated.txt'
    with open('selected_conversations') as file, open(output_file, 'w', encoding = 'utf-8', errors='ignore') as output:
        for line in file:
            data = json.loads(line)
            post_list = data['post_list']
            if post_list:
                post_id = post_list[0]['post_id']
                post_type = post_list[0]['post_type']
                text = post_list[0]['text']
                html = post_list[0].get('html', '')
            
                if post_type == wantedPostType and not contains_chinese(text):
                    containsKeyword = False
                    for i in keywords:
                        for j in excludedWords:
                            if i.upper() in text.upper() and not (j.upper() in text.upper()):
                                containsKeyword = True
                                break
                    if containsKeyword:
                        entry = {
                            'post_id': post_id,
                            'text': text,
                            'html': html,
                            'labels' : []
                        }
                        #use openaiAPI to get labels:

                        #create prompt
                        labelList = []
                        post_text = entry['text']
                        myPrompt = f"Classify the github post with the post text\n\"{post_text}\"\nwith respect to how the text indicates the poster UTILIZED chatGPT in their software development with one of the following label choices. Criteria for choosing each label is provided:\n\n"
                        for label, description in label_choices.items():
                            myPrompt += f"{label}: {description}\n"
                        myPrompt += "\nRemember, the post text must clearly indicate that it fits one of the labels other than \'Unrelated\'. Otherwise, label it as Unrelated.\
 For example, if only a url or a few vague words are provided, choose \'Unrelated\'.\
 Respond with only the labels in brackets. Leave out the criteria and any symbols. For example, sometimes you respond with \'Unrelated.\' when you should just respond with \'Unrelated\'"

                        response = None
                        while True:
                            try:
                                response = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                    {"role": "user", "content": myPrompt}
                                    ]
                                )
                                break
                            except openai.error.RateLimitError:
                                # Handle RateLimitError
                                print("Rate limit reached. Waiting for the next available request slot...")
                                time.sleep(30)  # Delay before making the next request
                                response = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                    {"role": "user", "content": myPrompt}
                                    ]
                                )
                                break
                            except openai.error.APIError:
                                print("API Error. Delaying for another request...")
                                time.sleep(30)  # Delay before making the next request
                                response = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                    {"role": "user", "content": myPrompt}
                                    ]
                                )
                                break
                            except openai.error.ServiceUnavailableError:
                                print("Service Unavailable Error. Delaying for another request...")
                                time.sleep(30)  # Delay before making the next request
                                response = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                    {"role": "user", "content": myPrompt}
                                    ]
                                )
                                break
                        newLabel = response.choices[0].message.content
                        
                        labelList.append(newLabel)
                        entry = {
                            'post_id': post_id,
                            'text': text,
                            'html': html,
                            'labels' : labelList
                        }
                        output.write(json.dumps(entry) + "\n")
                        numOfType += 1

                if numOfType > 49:
                    break