import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_path = "db/lesson.db"

conn = sqlite3.connect(db_path)

query = """
SELECT 
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

plt.figure(figsize=(8, 5))
plt.plot(df['order_id'], df['cumulative'], color='purple', marker='.')
plt.title('Cumulative Revenue by Order')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.grid(True)
plt.show()