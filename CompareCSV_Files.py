import pandas as pd


df1 = pd.read_csv('OldFile.csv')

df2 = pd.read_csv('NewFile.csv.zip')

result = df1.apply(tuple, 1).isin(df2.apply(tuple, 1))
print(result)