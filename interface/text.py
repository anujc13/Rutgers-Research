import pandas as pd
import csv

df = pd.read_csv('sample.csv')
mip = df[:15]
lD = df[15:]
keywords = ['abortion','african american','big','black','budget','characteristic','court','crime','debt','deficit','economy','economical','education','efficient','efficiency','employment','unemployment','employ','employed','unemployed','environment','gay','group','gun','health','hispanic','homosexual','ideology','ideological','ideologies','inflation','issue','middle','minority','philosophy','policy','policies','political','politics','poor','rate','rights','small','business','spend','tax','union','veteran','wealth','welfare','women']
output = ''
merge = []
questions = []
questions2 = []
for type in lD['Question']:
    if 'dislike' in type:
        questions.append('Question: Is there anything in particular that you dislike about the Democratic party?')

for type in mip['Question']:
    if 'imp' in type:
        questions2.append("Question: What is the most important national problem?")
    
def do(input):
    return "<span class='key' style='color: red'>{}</span>".format(input)
    
for text in mip['Text']:
    words = text.split()
    output = ''
    for word in words:
        if word.lower() in keywords:
            output += do(word) + ' '

        else:
            output += word + ' '
    merge.append(output)

lD = list(lD['Text'])
dictionary = {'Text': lD, 'alteredText': merge, 'AffectQuestions': questions, 'MIPQuestions': questions2}
dictionary = pd.DataFrame.from_dict(dictionary)

dictionary.to_csv('sample2.csv')



