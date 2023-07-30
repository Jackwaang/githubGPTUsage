
import json


postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']

#load stored labels into entries dict
entriesDict = dict()
with open('stored_labels.txt') as file:
    for line in file:
            data = json.loads(line)
            entriesDict[data['post_id']] = data['labels']

#go through files and modify labels with stored labels. store not in entriesDict as empty

#To do this, go through openaigenerated. For each line. look if id is in entries dict. 
#If it is, have entries label be set to the labels in the dict
#If not, have entry be unrelated.
#Then, add entry to list of entries
#after going through every line in file, write list of entries json dump to the non_openaigenerated file.
for type in postTypes:
    entriesList = []
    file1name = type + '.txt'
    file2name = type + '_openaiGenerated.txt'
    with  open(file2name) as file2:
        for line in file2:
            data = json.loads(line)
            if(data['post_id'] in entriesDict):
                 data['labels'] = entriesDict[data['post_id']]
            else:
                 data['labels'] = ['TO_RESOLVE']
            entriesList.append(json.dumps(data))

    with open(file1name, 'w', encoding = 'utf-8', errors='ignore') as output:
         for entry in entriesList:
              output.write(entry + '\n')

