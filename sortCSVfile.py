import pandas as pd

df = pd.read_csv("dictionaryedited1.csv")

# print(df)

df.columns = ['word']
df['wordLength'] = df['word'].str.len()
dff = df.sort_values('wordLength', ascending=False, inplace=False)

dff = dff[dff['word'].str.contains(" ") == False]
dff = dff.drop(columns=['wordLength'])
print(dff)

#dff.to_csv('dictionaryPreprocessed.csv',header=False,index=False)

