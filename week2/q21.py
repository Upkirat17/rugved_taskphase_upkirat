import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

matches=pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

highest_mom_winners=matches['player_of_match'].value_counts().nlargest(10)
# print(highest_mom_winners)

sns.barplot(x=highest_mom_winners.index,  y= highest_mom_winners.values)
plt.title("Highest MOM Award Winners")
plt.xlabel("Name of player")
plt.ylabel("Number of MOM Awards")
plt.show()

# plt.bar(x=highest_mom_winners.index,  height= highest_mom_winners.values)
# plt.title("Highest MOM Award Winners")
# plt.xlabel("Name of player")
# plt.ylabel("Number of MOM Awards")
# plt.show()

# This is the way to do it without seaborn. Define the y-axis by using the "height" attribute.