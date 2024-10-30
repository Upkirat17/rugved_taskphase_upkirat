import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

deliveries=pd.read_csv('/home/upkirat/Documents/rugved/python/deliveries.csv')

dismissal_count=deliveries['dismissal_kind'].value_counts()

x_values=np.arange(len(dismissal_count))

print(x_values)

sns.regplot(x=x_values, y= dismissal_count.values , scatter=True, fit_reg=True)


plt.xticks(ticks=x_values, labels=dismissal_count.index, rotation=45)

plt.title("Dismissal Kind Distribution with Best Fit Line")
plt.xlabel("Dismissal Kind")
plt.ylabel("Count")
plt.show()
