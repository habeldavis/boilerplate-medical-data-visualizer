import pandas as pd

df=pd.read_csv('medical_examination.csv')

for i in df.columns:
    print(df[i].value_counts())