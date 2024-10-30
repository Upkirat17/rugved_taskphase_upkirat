import pandas as pd
import numpy as np

df=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

toss_winner=df['toss_winner'].value_counts()

print(toss_winner)