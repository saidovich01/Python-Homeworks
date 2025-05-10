# Homework-1

# Task-1
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///chinook.db")

invoices = pd.read_sql_table("invoices", engine)

# 1-1
total_amount = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# print(total_amount)

# 1-2
top_5 = total_amount.sort_values(by="Total", ascending=False).head(5)

# print(top_5)

# 1-3
customers = pd.read_sql_table("customers", engine)

join = pd.merge(top_5, customers, on="CustomerId")

result = join[["CustomerId", "FirstName", "LastName", "Total"]]

# print(result)


##################################################################################


# Task-2
# 2-1
albums = pd.read_sql_table("albums", engine)
tracks = pd.read_sql_table("tracks", engine)


tracks.merge(albums, how="outer", on="AlbumId")

sum_tracks = tracks.groupby("AlbumId")["TrackId"].count()

print(sum_tracks)
