import pandas as pd
import numpy as np

df = pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

no_of_matches = df[df['season'] == 2008].shape[0]

print("Number of matches held in 2008:", no_of_matches)