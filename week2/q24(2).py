import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load matches data
matches = pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

# Distribution of matches won by each team
plt.figure(figsize=(10, 6))
sns.histplot(matches['winner'], bins=len(matches['winner'].unique()), kde=True)
plt.title("Distribution of Matches Won by Each Team")
plt.xlabel("Team")
plt.ylabel("Count of Wins")
plt.xticks(rotation=45)
plt.show()
