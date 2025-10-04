import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_path = "db/lesson.db"

conn = sqlite3.connect(db_path)

query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o 
    ON e.employee_id = o.employee_id
JOIN line_items l 
    ON o.order_id = l.order_id
JOIN products p 
    ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

employee_results = pd.read_sql_query(query, conn)

conn.close()

print(employee_results)

employee_results = employee_results.sort_values("revenue", ascending=False)

employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    legend=False,
    color="orange",
    figsize=(8,6)
)

plt.xlabel("Employee")
plt.ylabel("Revenue")
plt.title("Revenue by Employee")
plt.xticks(rotation=45, ha="right")

plt.show()