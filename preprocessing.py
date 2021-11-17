# Data Cleaning
# November 2, 2021

# %% matplotlib inline
# first, let's import all necessary modules & assign aliases
import os
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime as dt

# Preprocessing
# Find out what the current directory is
print(os.getcwd())
 
df = pd.read_csv("C:/Users/megan/OneDrive/Desktop/covid_pharm_data/data.csv", index_col = 0, header = [0, 1])
df.head()

# %%
df.index = pd.to_datetime(df.index)
companies = ['PFIZER', 'ASTRAZENECA', 'BIONTECH', 'MODERNA', 'NOVAVAX']

# %%
# make separate  dataframes for each company in companies
pfizer = df["PFIZER"]
pfizer.head()

astrazeneca = df["ASTRAZENECA"]
astrazeneca.head()

biontech = df["BIONTECH"]
biontech.head()

moderna = df["MODERNA"]
moderna.head()

novavax = df["NOVAVAX"]
novavax.head()


# %%
# make the correlation matrix
prices = pd.DataFrame()
for i in companies:
  prices[i] = df[i]['Close']
prices.corr()

# %%
# heatmap using seaborn to illustrate correlations
#sns.color_palette("mako", as_cmap=True)
fig = plt.figure(figsize=(7,6))
sns.heatmap(prices.corr(), annot=True, cmap='mako', linewidths=0.2, vmin=0, vmax=1)

# %%
# type(pfizer.Close)
# set our variables -- use .to_numpy() to format as ndarray
# pfizer.index = pd.to_datetime(pfizer.index)
# x = pfizer.index.to_numpy()
# type(x)
# print(pfizer.index)
# linear regression doesn't work on datetime data

# pfizer.index = pd.to_datetime(pfizer.index)
# pfizer.index.datetime.toordinal()
# x = pfizer.index.to_julian_date().to_numpy()
# type(x)
# print(pfizer.index)

x = moderna.Close.to_numpy()

# %%
y = pfizer.Close.to_numpy()
type(y)
print(pfizer.Close)


# %%
p = LinearRegression().fit([x, y])

# %%
