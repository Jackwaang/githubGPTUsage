
import json


postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']

entriesList = []

for postType in postTypes:
    input_file = postType + '.txt'
    with open(input_file) as file:
        for line in file:
            data = json.loads(line)
            entry = {
                'post_id': data['post_id'],
                'labels': data['labels']
            }
            entriesList.append(json.dumps(entry))

with open('stored_labels.txt', 'w', encoding = 'utf-8', errors='ignore') as output:        
    for entry in entriesList:
        output.write(entry + '\n')