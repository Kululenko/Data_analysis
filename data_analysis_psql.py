import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:sihing123@localhost:5432/salesanalysis")

df = pd.read_csv("c:/Users/pcmai/Desktop/python/data_analysis/SalesData.csv")

df.columns = [c.lower() for c in df.columns]

df.to_sql("sales",engine, if_exists="replace",index=False)


query = """
SELECT
    SUM(price*quantity) AS total_sales
    AVG(price) AS average_price
    SUM(quantity) AS total_units_sold
FROM
    sales;
"""

df2 = pd.read_sql(query,engine)
print(df2)