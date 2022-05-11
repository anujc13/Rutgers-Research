import pandas as pd
import numpy as np

nom_dat = pd.read_csv("https://voteview.com/static/data/out/members/HSall_members.csv")

south = [x for x in range(40,50)]
south.append(51)
south.append(53)

polar_dat = nom_dat[(nom_dat['congress'] > 45) & (nom_dat['chamber'] != 'President')]
nom_dat['year'] = 2*nom_dat['congress'] - 1 + 1789

nom_dat.groupby(['chamber','congress','year'])['nominate_dim1'].agg(['mean'])