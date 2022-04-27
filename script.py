#%% start something

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import interp1d

# import dataset
df = pd.read_csv('data/airspace_combined_table.csv')

# change date to time
df['date'] = df['date'].astype('datetime64')

# select date from Dec. 1st to the end
df = df[df['date'] >= '2021-12-01']

# select two columns - house-1-rehs-data / morality
df = df[['date', 'house-1-rehs-data', 'motality']]

# substitute nan with 0
df = df.replace(np.nan, 0)

# set date as index
df.set_index('date', inplace=True)

# change format of date
df.index = df.index.strftime('%Y-%m-%d')

# draw one plot
# plt.plot(df['house-1-rehs-data'])
# plt.show()

# set fig and ax
fig, ax = plt.subplots(1, 1, figsize=(20, 7))

# set title
ax.set_title("ReHS vs. Morality ")

# draw bar chart
p1 = sns.barplot(ax=ax, x=df.index, y='motality',
                 data=df,
                 ci=None,
                 color='lightsteelblue')

# set twinx()
ax = ax.twinx()

# set line chart
p2 = sns.lineplot(ax=ax, x=df.index, y='house-1-rehs-data',
                 data=df,
                 ci=None,
                 color='red',
                 marker='o')

p1.set_label('morality')
p2.set_label('ReHS')

# plt.show()
plt.savefig('./1.png')