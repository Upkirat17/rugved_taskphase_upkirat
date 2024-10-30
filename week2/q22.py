import pandas as pd
import numpy as np

matches=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

total_matches=matches['team1'].value_counts() + matches['team2'].value_counts()


print(total_matches)