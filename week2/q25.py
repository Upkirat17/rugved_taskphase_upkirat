import pandas as pd

matches=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

total=matches['team1'].value_counts() + matches['team2'].value_counts()
won=matches['winner'].value_counts()


ratio_df=pd.DataFrame({"Matches Played":total, "Matches Won":won})
ratio_df['win_ratio']=ratio_df['Matches Won']/ratio_df['Matches Played']
print(ratio_df)