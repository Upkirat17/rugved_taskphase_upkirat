import pandas as pd
import numpy as np

df = pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

all_umpires = pd.concat([df['umpire1'], df['umpire2'], df['umpire3']])

ump_count=all_umpires.value_counts()

goat_ump=ump_count.idxmax()
goat_matches_count= ump_count.max()

print(goat_ump, "-", goat_matches_count, "matches umpired.")
print(goat_ump, "is the goat fr")