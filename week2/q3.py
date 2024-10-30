import pandas as pd

df=pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

city_wise_matches=df.groupby('city').size()

print(city_wise_matches)