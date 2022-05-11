import pandas as pd

df = pd.read_csv('sample.csv')
adj = []
output = ''
merge = []
keywords = ['abortion','african american','big','black','budget','characteristic','court','crime','debt','deficit','economy','economical','education','efficient','efficiency','employment','unemployment','employ','employed','unemployed','environment','gay','group','gun','health','hispanic','homosexual','ideology','ideological','ideologies','inflation','issue','middle','minority','philosophy','policy','policies','political','politics','poor','rate','rights','small','business','spend','tax','union','veteran','wealth','welfare','women']

for text in df['mip1']:
    if text != '' and isinstance(text,str):
        adj.append(text)
    

def do(input):
    return "<span class='key' style='color: red'>{}</span>".format(input)

for x in range(25, len(adj), 50):
    text = adj[x]
    if len(text) > 132:
        words = text.split()
        output = ''
        for word in words:
            if word.lower() in keywords:
                output += do(word) + ' '
            else:
                output += word + ' '
        merge.append(output)
    
    

dictionary = {'text': merge}
    
dictionary = pd.DataFrame.from_dict(dictionary)

dictionary.to_csv('mip.csv')



