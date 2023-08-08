#A Program to run to perform analysis on collected data.


import json

postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']
list1 = []
list2 = []
textList1 = []
labels = ['Code Generation', 'Code Review', 'Code summarization', 'GPT Integration', 'Test Case Generation', 'Unrelated']


for type in postTypes:
    file1name = type + '.txt'
    file2name = type + '_openaiGenerated.txt'
    with open(file1name) as file1, open(file2name) as file2:
        for line in file1:
            data = json.loads(line)
            list1.append((data['labels'], type))
            textList1.append([data['text'], file1name])
        for line in file2:
            data = json.loads(line)
            list2.append((data['labels'], file2name))

numEqual = 0
numUnrelated = 0
#loop through nonopenai posts
for i in range(0, (len(list1))):
    #loop through manual labels
    for j in range(0, len(list1[i][0])):
        #loop through labels in openaiGenerated file
        for k in range(0, len(list2[i][0])):
            manualLabel = list1[i][j]
            AILabel = list2[i][k]
            if manualLabel == AILabel:
                numEqual += 1
            else:
                
                print(textList1[i][0] + " in file " + textList1[i][1])
                print("Manual label(s) ")
                print(list1[i][0])
                print("AI Labels: ")
                print(list2[i][0])
                print("\n" )
                
        if list1[i][j] == ['Unrelated']:
            numUnrelated += 1

#Loop through each post type and each label to figure out label distribution
#loop through postTypes
with open('results.txt', 'w', encoding = 'utf-8', errors='ignore') as output:
    for type in postTypes:
        output.write("For file type: " + type + "\n")
        numOfType = 0
        #loop through each Label
        for label in labels:
            numOfLabel = 0
            #loop through the manual labels
            for i in range(0, len(list1)):
                if(list1[i][1] == type):
                    #make sure it only increments on the first iteration
                    if(label == labels[0]):
                        numOfType += 1
                    for manualLabel in list1[i][0]:
                        if manualLabel == label:
                            numOfLabel += 1
            output.write(str(numOfLabel) + " posts are labeled as: " + label + '\n')

        output.write("of " + str(numOfType) + " posts of type " + type + "\n" )

        

    output.write(str(numEqual) + '/' + str(len(list1)) + ' are matching, ')
    output.write(str(numUnrelated) + '/' + str(len(list1)) + ' are Unrelated')

