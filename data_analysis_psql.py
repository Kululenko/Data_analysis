import pandas as pd
from sqlalchemy import create_engine

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