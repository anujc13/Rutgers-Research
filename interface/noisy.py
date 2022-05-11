import pandas as pd
import numpy as np

df = pd.read_csv('sample.csv')
df.to_csv('sample2.csv')

adj = []
merge = []
lst = ['(', ')']
noisy = set(lst)
temp = []

for text in df['mip1']:
    if text != '' and isinstance(text,str):
        adj.append(text)
#
#
#for x in range(len(adj)):
#    text = adj[x]
#    if (len(text) > 500):
#        for word in text.split():
#            if not(bool((len(noisy.intersection(set(list(word)))) > 0))):
#                merge.append(text.strip())
#                break
#            
#
#
#dictionary = {'text': merge}
#    
#dictionary = pd.DataFrame.from_dict(dictionary)
#
#dictionary[:51].to_csv('mip.csv')

for x in range(len(adj)):
    text = adj[x]
    for word in text.split():
        if bool((len(noisy.intersection(set(list(word)))) > 0)):
            for char in word:
                if (len(word) < 5 and len(word) > 3) and word[3] == ')':
                    temp.append(word)

print(np.unique(np.array(temp)))