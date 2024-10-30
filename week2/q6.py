import pandas as pd
import numpy as np

df=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

tie=df[df.result=='tie'].index.size
print('number of ties=', tie)


normal=df[df.result=='normal'].index.size
print('normal matches=',normal)