import pandas as pd

df=pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

print(df[df['result'] == 'tie'])