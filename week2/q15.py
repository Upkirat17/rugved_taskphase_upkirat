import pandas as pd
import numpy as np

df = pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

matches_played_in_season=df['season'].value_counts()
print(matches_played_in_season)