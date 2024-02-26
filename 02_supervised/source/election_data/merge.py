import pandas as pd


import pandas as pd

# For df_candidate
df_candidate = pd.read_csv('candidate_no_fada.csv', encoding='iso-8859-1')

print(df_candidate.head())

df = df_candidate.groupby(["Constituency", "Party Id"]).agg({"Votes": "sum"}).reset_index()

df['Vote Fraction'] = df['Votes'] / df.groupby('Constituency')['Votes'].transform('sum')

print(df.head())
