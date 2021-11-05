import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import plotnine
import seaborn as sns

df = pd.read_csv(r'C:\Users\qures\Downloads\Pharmaceutical companies on the stock exchange in 2020 (2).csv', index_col=0 ,header=[0,1])
df.head()
df.dtypes

df.index = pd.to_datetime(df.index)
df.dtypes

df.isnull().values.any()


pfizer= df["PFIZER"]
astrazeneca= df["ASTRAZENECA"]
moderna= df["MODERNA"]
novavax= df["NOVAVAX"]

print(df.loc['2020-01-01':'2020-01-31'])
