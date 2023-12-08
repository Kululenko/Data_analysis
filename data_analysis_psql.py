import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns




engine = create_engine("postgresql://postgres:sihing123@localhost:5432/salesanalysis")

df = pd.read_csv("c:/Users/pcmai/Desktop/python/data_analysis/SalesData.csv")

df.columns = [c.lower() for c in df.columns]

df.to_sql("sales",engine, if_exists="replace",index=False)


query1 = """
SELECT
    SUM(price*quantity) AS total_sales,
    AVG(price) AS average_price,
    SUM(quantity) AS total_units_sold
FROM
    sales;
"""
query2 = """
SELECT product_id, SUM(price*quantity) AS total_sales
FROM sales
GROUP BY product_id
ORDER BY total_sales desc;
"""
query3 = """
SELECT sale_date, AVG(price*quantity) AS average_daily_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
"""
query4 = """
SELECT sale_date, SUM(price*quantity) AS total_sales
FROM sales
GROUP BY sale_date
ORDER BY total_sales DESC
LIMIT 10;
"""

df1 = pd.read_sql(query1,engine)
print(df1)
df2 = pd.read_sql(query2, engine)
print(df2)
df3 = pd.read_sql(query3, engine)
print(df3)
df4 = pd.read_sql(query4, engine)
print(df4)


#visualising my querys // Gesamtumsatz pro Produkt
plt.figure(figsize=(10,6))
sns.barplot(x="product_id", y="total_sales", data=df2)
plt.title("Gesamtumsatz pro Produkt")
plt.xlabel("Product_ID")
plt.ylabel("Gesamtumsatz")
plt.xticks(rotation=45)
plt.show()

#Durchschnittlicher Verkaufswert pro Tag
plt.figure(figsize=(10,6))
sns.lineplot(x="sale_date", y="average_daily_sales", data=df3)
plt.title("Durchschnittlicher Verkaufswert pro Tag")
plt.xlabel("Datum")
plt.ylabel("Durchschnittlicher Verkaufswert")
plt.xticks(rotation=45)
plt.show()

#Top Verkaufstage
plt.figure(figsize=(10,6))
sns.barplot(x="sale_date", y="total_sales", data=df4)
plt.title("Top Verkaufstage")
plt.xlabel("Datum")
plt.ylabel("Gesamtumsatz")
plt.xticks(rotation=45)
plt.show()

#showing top sales and lowest sales
top10 = df2.head(10)
bot10 = df2.tail(10)

topbot_10 = pd.concat([top10,bot10])

plt.figure(figsize=(12,8))
sns.barplot(x="product_id", y="total_sales", data=topbot_10)
plt.title("Top 10 and bot nach Umsatz")
plt.xlabel("Product_id")
plt.ylabel("Gesamtumsatz")
plt.xticks(rotation=90)
plt.show() 