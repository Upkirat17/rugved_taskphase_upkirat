import pandas as pd
import numpy as np  

df=pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

win_runs=df[['winner','win_by_runs']]

winner=win_runs.loc[win_runs['win_by_runs'].idxmin()]

print(winner)