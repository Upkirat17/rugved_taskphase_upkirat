import pandas as pd
import matplotlib.pyplot as plt

matches=pd.read_csv("/home/upkirat/Documents/rugved/python/matches.csv")

choice=matches.groupby(['toss_winner','toss_decision']).size().unstack()

choice.plot(kind="bar", figsize=(10,10), stacked=True)
plt.xlabel("Team")
plt.ylabel("Toss Decision")
plt.legend(["Heads","Tails"], title="Decision")
plt.show()
