import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

# ----------------------------------------
# Step 1: First five employees
# ----------------------------------------
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
LIMIT 5;
""", conn)


# ----------------------------------------
# Step 2: Reverse columns
# ----------------------------------------
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
LIMIT 5;
""", conn)


# ----------------------------------------
# Step 3: Alias example
# ----------------------------------------
df_alias = pd.read_sql("""
SELECT lastName AS surname, employeeNumber AS id
FROM employees
LIMIT 5;
""", conn)


# ----------------------------------------
# Step 4: Executive employees (example filter)
# ----------------------------------------
df_executive = pd.read_sql("""
SELECT *
FROM employees
WHERE jobTitle LIKE '%Executive%';
""", conn)


# ----------------------------------------
# Step 5: Name length
# ----------------------------------------
df_name_length = pd.read_sql("""
SELECT lastName, LENGTH(lastName) AS name_length
FROM employees;
""", conn)


# ----------------------------------------
# Step 6: Short titles
# ----------------------------------------
df_short_title = pd.read_sql("""
SELECT jobTitle
FROM employees
WHERE LENGTH(jobTitle) < 20;
""", conn)


# ----------------------------------------
# Step 7: Total price from orderDetails
# ----------------------------------------
df_total_price = pd.read_sql("""
SELECT quantityOrdered * priceEach AS total_price
FROM orderDetails;
""", conn)

sum_total_price = df_total_price["total_price"].sum()


# ----------------------------------------
# Step 8: Date breakdown
# ----------------------------------------
df_day_month_year = pd.read_sql("""
SELECT 
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders;
""", conn)


conn.close()