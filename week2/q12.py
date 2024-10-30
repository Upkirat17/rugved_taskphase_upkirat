import pandas as pd
import numpy as np

df=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')


# win_runs=df[['winner','win_by_runs','venue']]

# winner=win_runs.loc[win_runs['win_by_runs'].idxmax()]

# print(winner)

max_run_win_index = df['win_by_runs'].idxmax()

venue=df.loc[max_run_win_index,'venue']

print(venue)