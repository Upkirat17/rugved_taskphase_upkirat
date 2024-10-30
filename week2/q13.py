import pandas as pd
import numpy as np

df=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')


min_run_win_index = df['win_by_runs'].idxmin()

venue=df.loc[min_run_win_index,'venue']

print(venue)