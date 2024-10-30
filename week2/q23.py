import pandas as pd

matches=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

total_matches=matches['team1'].value_counts() + matches['team2'].value_counts()

winning_matches=matches['winner'].value_counts()

win_rate= (winning_matches/total_matches)*100

comparison=pd.DataFrame({"Matches Played": total_matches, "Matches won": winning_matches,"Win rate": win_rate})

print(comparison)