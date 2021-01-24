import pandas as pd

df_chimie = pd.read_csv('chimie_edited.csv', delimiter=',')

# trouver les valeurs les plus recherchées
df_count_chimie = df_chimie['CdParametre'].value_counts()
df_count_chimie.to_csv('count_chimie.csv')
