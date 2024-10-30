import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


deliveries = pd.read_csv('/home/upkirat/Documents/rugved/python/deliveries.csv')

top_scorer=deliveries.groupby('batsman')['batsman_runs'].sum().nlargest(10)
# print(top_scorer)

x_values=np.arange(len(top_scorer))

sns.regplot(x=x_values, y= top_scorer.values , scatter=True, fit_reg=True)
plt.xticks(ticks=x_values, labels=top_scorer.index, rotation=45)
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Batsman")
plt.ylabel("Total Runs")
plt.show()