
import json
from pathlib import Path


#Program to store the labels in the nonOpenAIGenerated files to be applied in later runs.

postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']

current_directory = Path(__file__).resolve().parent
parent_directory = current_directory.parent
subfolder_name = "data"
subfolder_path = parent_directory / subfolder_name
text_file_name = "stored_manual_labels.txt"
text_file_path = str(subfolder_path / text_file_name)

entriesDict = dict()
#First, store the labels already in stored_labels
with open(text_file_path) as input:
    for line in input:
        data = json.loads(line)
        entry = {
                'post_id': data['post_id'],
                'labels': data['labels']
        }
        entriesDict[data['post_id']] = (json.dumps(entry))

#Then, go through and add new labels. 
for postType in postTypes:
    inputFileName = postType + '.txt'
    manualLabelsFolder = "manuallyLabeledFiles"
    inputFilePath = parent_directory / manualLabelsFolder / inputFileName
    with open(inputFilePath) as file:
        for line in file:
            data = json.loads(line)
            entry = {
                'post_id': data['post_id'],
                'labels': data['labels']
            }
            if ('TO_RESOLVE' not in data['labels']):
                entriesDict[data['post_id']] = json.dumps(entry)


#Go through dictionary and write to file.
with open(text_file_path, 'w', encoding = 'utf-8', errors='ignore') as output:        
    for entry in entriesDict.values():
        output.write(str(entry) + '\n')
        