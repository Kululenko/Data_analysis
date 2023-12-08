import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# machine learning
engine = create_engine("postgresql://postgres:sihing123@localhost:5432/salesanalysis")

df = pd.read_sql("SELECT * FROM sales", engine)

df["total_sales"] = df["price"] * df["quantity"]

X = df[["product_id","price","quantity"]]
y = df["total_sales"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test,y_pred))
print("Coefficient of dtermination (R^2):", r2_score(y_test,y_pred))


print(df.describe())


sns.histplot(df["price"], kde=True)
plt.show()

sns.countplot(x="product_id", data=df)
plt.show()

corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

sns.pairplot(df)
plt.show()