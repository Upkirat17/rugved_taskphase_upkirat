import pandas as pd

# Load matches and deliveries data
matches = pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')
deliveries = pd.read_csv('/home/upkirat/Documents/rugved/python/deliveries.csv')

# Merge the datasets on 'id' from matches and 'match_id' from deliveries
merged_data = pd.merge(deliveries, matches[['id', 'season']], left_on='match_id', right_on='id')

# Group by 'season' and sum the 'total_runs' to get the total runs per season
total_runs_per_season = merged_data.groupby('season')['total_runs'].sum()

# Print the result
print(total_runs_per_season)



#couldn't figure out how to do this on my own. Ended up using chatgpt and then learned how to merge tables.