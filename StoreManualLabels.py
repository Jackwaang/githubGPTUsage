
import json

#Program to store the labels in the nonOpenAIGenerated files to be applied in later runs.

postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']

entriesDict = dict()
#First, store the labels already in stored_labels
with open('stored_labels.txt') as input:
    for line in input:
        data = json.loads(line)
        entry = {
                'post_id': data['post_id'],
                'labels': data['labels']
        }
        entriesDict[data['post_id']] = (json.dumps(entry))

#Then, go through and add new labels. 
for postType in postTypes:
    input_file = postType + '.txt'
    with open(input_file) as file:
        for line in file:
            data = json.loads(line)
            entry = {
                'post_id': data['post_id'],
                'labels': data['labels']
            }
            if ('TO_RESOLVE' not in data['labels']):
                entriesDict[data['post_id']] = json.dumps(entry)


#Go through dictionary and write to file.
with open('stored_labels.txt', 'w', encoding = 'utf-8', errors='ignore') as output:        
    for entry in entriesDict.values():
        output.write(str(entry) + '\n')
        