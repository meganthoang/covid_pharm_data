# Data Cleaning
# November 2, 2021

# %% matplotlib inline
# first, let's import all necessary modules & assign aliases
import pandas as pd
import numpy as np
import os
import seaborn as sns
from matplotlib import pyplot as plt

# Preprocessing
# Find out what the current directory is
print(os.getcwd())

df = pd.read_csv("C:/Users/megan/OneDrive/Desktop/covid_pharm_data/data.csv", index_col = 0, header = [0, 1])
df.head()

# %%
df.index = pd.to_datetime(df.index)
companies = ['PFIZER', 'ASTRAZENECA', 'BIONTECH', 'MODERNA', 'NOVAVAX']

# %%
pfizer = df["PFIZER"]
pfizer.head()
# %%
astrazeneca = df["ASTRAZENECA"]
astrazeneca.head()
# %%
biontech = df["BIONTECH"]
biontech.head()
# %%
moderna = df["MODERNA"]
moderna.head()
# %%
novavax = df["NOVAVAX"]
novavax.head()

# %%
# make the correlation matrix
prices = pd.DataFrame()
for i in companies:
  prices[i] = df[i]['Close']
prices.corr()

# %%
# heatmap using seaborn
fig = plt.figure(figsize=(10,8))
mask = np.zeros_like(preço_ativos.corr())
mask[np.triu_indices_from(mask)] = True
sns.heatmap(preço_ativos.corr(), annot=True, cmap='Blues', linewidths=0.2, mask=mask, vmin=0, vmax=1)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11);
