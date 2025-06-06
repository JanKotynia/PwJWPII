import sqlite3
import pandas as pd
con = sqlite3.connect("sales.db")
# cursor = con.cursor()
# cursor.execute("SELECT * FROM sales")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
    
df = pd.read_sql("SELECT * FROM sales", con)
print(df)
print(">---------------------------------------------<")
df = pd.read_sql("SELECT * FROM sales WHERE product=='Laptop'", con)
print(df)
print(">---------------------------------------------<")
df = pd.read_sql("SELECT * FROM sales WHERE date='2025-05-07' OR date='2025-05-08'", con)
print(df)
print(">---------------------------------------------<")
df = pd.read_sql("SELECT * FROM sales WHERE price>200", con)
print(df)
print(">---------------------------------------------<")
df = pd.read_sql("SELECT product, SUM(price) FROM sales GROUP BY product", con)
print(df)
print(">---------------------------------------------<")
df = pd.read_sql("SELECT product, COUNT(product) AS value FROM sales GROUP BY product ORDER BY value DESC LIMIT 1", con)
print(df)
print(">---------------------------------------------<")
con.close()

