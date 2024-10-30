import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/home/upkirat/Documents/rugved/python/matches.csv')

toss_season=df.groupby(['season','toss_decision']).size().unstack()


# print(toss_season)

toss_season.plot(kind='bar', figsize=(10,5))
plt.title("Toss Decision Across Multiple Seasons")
plt.xlabel("Season")
plt.ylabel("Toss Decision")
plt.legend(['Bat','Ball'], title="Toss Decision")
plt.show()