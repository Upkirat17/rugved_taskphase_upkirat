import pandas as pd
import numpy as np

df=pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

toss_winner=df['toss_winner'].value_counts()

max=toss_winner.idxmax()
min=toss_winner.idxmin()
print("Team that won the toss max times - ", max)
print("Team that won the toss min times - ", min)