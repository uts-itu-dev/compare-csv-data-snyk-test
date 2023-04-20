import pandas as pd
import numpy as np


df1 = pd.read_csv('OldFile.csv')
df2 = pd.read_csv('NewFile.csv.zip')
df3 = pd.read_csv('NewFile.csv')

#Method 1
array1 = np.array(df1)
array2 = np.array(df2)

df_CSV_1 = pd.DataFrame(array1, columns=['ID', 'Name', 'Dob', 'Subject'])
df_CSV_2 = pd.DataFrame(array2, columns=['ID', 'Name', 'Dob', 'Subject'])

df_CSV_1.index += 1
df_CSV_2.index += 1

print(df_CSV_1.eq(df_CSV_2).to_string(index=True))
print("\n")

#Method 2
a = df1[df1.eq(df2).all(axis=1) == False]
a.index += 1
print(a.to_string(index=False))
print("\n")


#Method 3
df_diff = pd.merge(df1, df2, how="right", indicator="Exist")
print(df_diff)
print("\n")

df_diff2 = df_diff.query("Exist != 'both'")
print(df_diff2)
print("\n")