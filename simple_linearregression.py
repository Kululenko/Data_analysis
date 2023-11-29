import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


data = pd.read_csv("1.01.+Simple+linear+regression.csv")
print(data.describe())

y = data["GPA"]
x1 = data["SAT"]

plt.scatter(x1,y)
plt.xlabel("SAT", fontsize=20)
plt.ylabel("GPA", fontsize=20)
plt.show()

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
print(results.summary())



