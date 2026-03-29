import sqlite3
import pandas as pd

# ----------------------------------------
# STEP 1: Connect to SQLite database
# ----------------------------------------
conn = sqlite3.connect("data.sqlite")


# ----------------------------------------
# STEP 2: Read employees (basic query)
# ----------------------------------------
df_employees = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees;
""", conn)

print("=== Employees (First 5 Rows) ===")
print(df_employees.head())
print("\n")


# ----------------------------------------
# STEP 3: Reverse column selection
# ----------------------------------------
df_employees_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees;
""", conn)

print("=== Employees (Reversed Columns) ===")
print(df_employees_reverse.head())
print("\n")


# ----------------------------------------
# STEP 4: Orders date breakdown (FIXED)
# ----------------------------------------
df_orders_date = pd.read_sql("""
SELECT 
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders;
""", conn)

print("=== Orders (Day, Month, Year) ===")
print(df_orders_date.head())
print("\n")


# ----------------------------------------
# STEP 5: Example join (orders + orderDetails)
# ----------------------------------------
df_join = pd.read_sql("""
SELECT 
    o.orderNumber,
    o.orderDate,
    od.productCode,
    od.quantityOrdered,
    od.priceEach
FROM orders o
JOIN orderDetails od
    ON o.orderNumber = od.orderNumber;
""", conn)

print("=== Orders Joined with Order Details ===")
print(df_join.head())
print("\n")


# ----------------------------------------
# STEP 6: Close connection
# ----------------------------------------
conn.close()