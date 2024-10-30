import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

plt.figure(figsize=(10,6))
sns.histplot(matches['winner'], bins=len(matches['winner'].unique()), kde=True)
plt.xlabel("Winner")
plt.ylabel("Winning Count")
plt.title("Distribution of Match Wins")
plt.xticks(rotation=90)
plt.show()