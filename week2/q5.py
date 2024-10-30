import pandas as pd
import numpy as np

df=pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

toss=df[['toss_winner', 'toss_decision']]

print(toss)
