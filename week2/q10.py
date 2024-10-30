import pandas as pd
import numpy as np

df=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

pom_counts=df['player_of_match'].value_counts()

required=pom_counts[pom_counts>3]

print(required)