import json

postTypes = ['issues', 'issues_comment', 'pull', 'pull_comment', 'pull_review_comment', 'commit_comment']
list1 = []
list2 = []
textList1 = []

for type in postTypes:
    file1name = type + '.txt'
    file2name = type + '_openaiGenerated.txt'
    with open(file1name) as file1, open(file2name) as file2:
        for line in file1:
            data = json.loads(line)
            list1.append([data['labels']])
            textList1.append([data['text'], file1name])
        for line in file2:
            data = json.loads(line)
            list2.append([data['labels']])

numEqual = 0
numUnrelated = 0
for i in range(0, (len(list1))):
    for j in range(0, len(list1[i])):
        for k in range(0, len(list2[i])):
            if list1[i][j] == list2[i][k]:
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
        

print(str(numEqual) + '/' + str(len(list1)) + ' are matching')
print(str(numUnrelated) + '/' + str(len(list1)) + ' are Unrelated')

