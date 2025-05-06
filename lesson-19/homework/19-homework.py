# Homework-1
import pandas as pd

sales = pd.read_csv("sales_data.csv")

# print(sales)

# Task-1

Analys = (sales.
          groupby("Category")
          .agg(
              total_quantity = pd.NamedAgg(column="Quantity", aggfunc="sum"),
              average_price = pd.NamedAgg(column="Price", aggfunc="mean"),
              max_quantity = pd.NamedAgg(column="Quantity", aggfunc="max")
          )
          .reset_index()
)

print(Analys)


# Task-2

Analys2  = sales.groupby(["Category", "Product"]).agg({"Quantity" : sum}).reset_index()

print(Analys2)


# Task-3
sales["Total Sales"] = sales["Price"] * sales["Quantity"]

Analys3 = sales.groupby("Date")["Total Sales"].sum()

print(Analys3)




###############################################################################


# Homework-2
import pandas as pd
customer = pd.read_csv("customer_orders.csv")

print(customer)

# Task-1
    
df = (customer
         .groupby("CustomerID")
         .agg(over_20 = pd.NamedAgg(column="OrderID", aggfunc="count")
         )
         .reset_index()
)

con = df["over_20"] > 20
print(df.loc[con])



# Task-2
df = (customer
      .groupby("CustomerID")
      .agg(over_120 = pd.NamedAgg(column="Price", aggfunc="mean"))
      .reset_index()
)

condition = df["over_120"] > 120

print(df.loc[condition])



# Task-3
df = (customer
      .groupby("Product")
      .agg(total_quantity = pd.NamedAgg(column="Quantity", aggfunc="sum"),
           total_price = pd.NamedAgg(column="Price", aggfunc="sum"))
      .reset_index()
)

condition = df["total_quantity"] >= 5

print(df.loc[condition])



# Homework-3
import sqlite3
import pandas as pd

conn = sqlite3.connect("population.db")

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
# print(tables)


df = pd.read_sql_query("SELECT * FROM population", conn)

print(df)

count_total = df["id"].count()

condition1 = df["salary"] <= 200000
count1 = df[condition1].count()

print(count1 / count_total * 100)


condition1 = df["salary"] <= 200000




