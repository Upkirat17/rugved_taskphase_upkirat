import pandas as pd


df = pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

matches = df['city'].value_counts()

max_matches=matches.max()
min_matches=matches.min()
city_max=matches.idxmax()
city_min=matches.idxmin()


print(city_max, "-", max_matches)
print(city_min,"-",min_matches)
print(matches)