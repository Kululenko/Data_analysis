import os
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

#print(os.getcwd())

data = pd.read_csv("c:/Users/pcmai/Desktop/python/data_analysis/real_estate_price_size.csv")

#check for missing values
print(data.isnull().sum())


print(data.describe())

x1 = data["size"]
y = data["price"]

plt.scatter(x1,y)
plt.xlabel("size", fontsize=20)
plt.ylabel("price", fontsize=20)
plt.show()

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
print(results.summary())
