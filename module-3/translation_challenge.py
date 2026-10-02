import sqlite3
import pandas as pd

sales_data = [
    ("Widget A", "Electronics", 29.99, 150, "2025-Q1"),
    ("Widget B", "Electronics", 49.99, 89, "2025-Q1"),
    ("Gadget X", "Accessories", 15.99, 300, "2025-Q1"),
    ("Widget A", "Electronics", 29.99, 200, "2025-Q2"),
    ("Gadget Y", "Accessories", 22.99, 175, "2025-Q2"),
    ("Widget C", "Electronics", 79.99, 50, "2025-Q2"),
    ("Gadget X", "Accessories", 15.99, 280, "2025-Q2"),
    ("Widget B", "Electronics", 49.99, 120, "2025-Q3"),
]

columns = ["product", "category", "unit_price", "quantity", "quarter"]


# 1. Load into a Pandas DataFrame
df = pd.DataFrame(sales_data, columns=columns)
print(df)

# 2. Connect to a SQLite database
connection = sqlite3.connect("sales.db")
connection.row_factory = sqlite3.Row

# 3. Put the DataFrame into a SQLite table
df.to_sql("sales", connection, if_exists="replace", index=False)


print("=== Q1: What is the total revenue (price × quantity) per product? ===")

# SQL approach:
sql_q1 = """
SELECT product, SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
"""
print("SQL result:")
for row in connection.execute(sql_q1):
    print(f"  {row['product']}: ${row['total_revenue']:.2f}")


# Pandas approach:
print("Pandas result:")
df["revenue"] = df["quantity"] * df["unit_price"]
pandas_q1 = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
pandas_q1.index.name = None
print(pandas_q1)


print("=== Q2: Which quarter had the highest total quantity sold? ===")

# SQL approach:
sql_q2 = """
    SELECT s.quarter, SUM(s.quantity) AS total_quantity
    FROM sales s
    GROUP BY s.quarter
    ORDER BY total_quantity DESC
    LIMIT 1
    """
row = connection.execute(sql_q2).fetchone()
print(f"SQL: {row['quarter']} — {row['total_quantity']} units")

# Pandas approach:
pandas_q2 = df.groupby("quarter")["quantity"].sum()
highest_quarter = pandas_q2.idxmax()
highest_quantity = pandas_q2.max()
pandas_q2.index.name = None

print(f"Pandas: {highest_quarter} — {highest_quantity} units")


print("=== Q3: What is the average unit price per category? ===")

# SQL approach:
sql_q3 = """
    SELECT category, AVG(unit_price) AS avg_unit_price 
    FROM sales 
    GROUP BY category
    """
print("SQL result:")
for row in connection.execute(sql_q3):
    print(f"  {row['category']}: ${row['avg_unit_price']:.2f}")

# Pandas approach:
print("Pandas result:")
pandas_q3 = (
    df[df["category"].notnull()].groupby("category")["unit_price"].mean().round(2)
)
pandas_q3.index.name = None
print(pandas_q3)


print("=== Q4: Which products had total quantity over 200 across all quarters? ===")

# SQL approach:
sql_q4 = """
    SELECT product, SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY product
    HAVING total_quantity > 200
    """
print("SQL result:")
for row in connection.execute(sql_q4):
    print(f"  {row['product']}: {row['total_quantity']} units")

# Pandas approach:
pandas_q4 = df.groupby("product")["quantity"].sum()
pandas_q4 = pandas_q4[pandas_q4 > 200]
pandas_q4.index.name = None
print("Pandas result:")
print(pandas_q4)


print(
    "=== Use pd.read_sql() to run one of your SQL queries and get the result as a DataFrame. ==="
)
sql_df = pd.read_sql(sql_q1, connection)
print(sql_df.to_string(index=False))

connection.close()
