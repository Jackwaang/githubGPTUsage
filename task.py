import json

keywords = ['chatGPT',
                 'code generation',
                 'code automation',
                 'automatic programming',
                 'automatically generated code',
                 'OpenAI',
                 'GPT 3',
                 'gpt 3.5',
                 'gpt 4',
                 'gpt',
                 'Codex',
                 'code completion',
                 'Copilot',
                 'AI generated code'
                ]

postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']

def contains_chinese(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False

for wantedPostType in postTypes:
    numOfType = 0
    output_file = wantedPostType + '.txt'
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
                        if i in text:
                            containsKeyword = True
                            break
                    if containsKeyword:
                        entry = {
                            'post_id': post_id,
                            'text': text,
                            'html': html,
                            'labels' : []
                        }
                        print(json.dumps(entry))
                        numLabels = int(input("How many labels\n"))
                        labelList = []
                        for i in range(numLabels):
                            labelIndex = int(input("1 = code generation\n 2 = code review\n 3 = code summarization \n 4 = gpt integration\n 5 = test case generation \n 6 = framework planning \n 7 = misc\n 8 = unrelated\n enter label:\n"))
                            newLabel = "Unrelated"
                            if labelIndex == 1:
                                newLabel = "Code Generation"
                            elif labelIndex == 2:
                                newLabel = "Code Review"
                            elif labelIndex == 3:
                                newLabel = "Code Summarization"
                            elif labelIndex == 4:
                                newLabel = "GPT Integration"
                            elif labelIndex == 5:
                                newLabel = "Test Case Generation"
                            elif labelIndex == 6:
                                newLabel = "Project Framework Planning"
                            elif labelIndex == 7:
                                newLabel = "Miscellaneous"
                            else:
                                newLabel = "Unrelated"
                            labelList.append(newLabel)
                        entry = {
                            'post_id': post_id,
                            'text': text,
                            'html': html,
                            'labels' : labelList
                        }
                        output.write(json.dumps(entry) + "\n")
                        numOfType += 1

                if numOfType > 50:
                    break

