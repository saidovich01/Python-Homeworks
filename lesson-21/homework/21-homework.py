# Homework
# DataFrame-1
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Ex-1
df1['Average_Grade'] = (df1['Math'] + df1['English'] +  df1['Science']) / 3
print(df1)

df1['Average_Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print(df1)

# Ex-2
df1['Average_Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)
max_avg = df1['Average_Grade'].max()
print(df1[df1['Average_Grade'] == max_avg])

# Ex-3
df1['Total'] = (df1['Math'] + df1['English'] +  df1['Science'])
print(df1)

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1)

# Ex-4
import matplotlib.pyplot as plt

x = ["Math", "English", "Science"]

math_avg = df1["Math"].mean()
eng_avg = df1["English"].mean()
science_avg = df1["Science"].mean()

y = [math_avg, eng_avg, science_avg]

plt.bar(x, y, width=0.5 , color=["r", "b", "g"])
plt.title("Subject Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()




# DataFrame-2
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Ex-1
df2["Total_sales"] = df2[["Product_A", "Product_B", "Product_C"]].sum(axis=1)

print(df2)

# Ex-2
Max_sale = df2["Total_sales"].max()

print(df2[df2['Total_sales'] == Max_sale])

# Ex-3
df2['Product_A_Change_%'] = df2['Product_A'].pct_change() * 100
df2['Product_B_Change_%'] = df2['Product_B'].pct_change() * 100
df2['Product_C_Change_%'] = df2['Product_C'].pct_change() * 100

print(df2)

# Ex-4
import matplotlib.pyplot as plt

plt.plot(df2['Date'], df2['Product_A'])
plt.plot(df2['Date'], df2['Product_B'])
plt.plot(df2['Date'], df2['Product_C'])

plt.title("Sales Trends for Each Product")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.show()



# DataFrame-3
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Ex-1
avg_salary = df3.groupby("Department")["Salary"].mean()
print(avg_salary)

# Ex-2
max_exp = df3["Experience (Years)"].max()

print(df3[df3['Experience (Years)'] == max_exp])

# Ex-3
df3["Salary Increase %"] = (df3["Salary"] - df3['Salary'].min()) / df3['Salary'].min() * 100

print(df3)

# Ex-4
import matplotlib.pyplot as plt

dept_counts = df3['Department'].value_counts()

# Plot the bar chart
plt.bar(dept_counts.index, dept_counts.values, color='orange')
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()



# DataFrame-4
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
print(df4)

# Ex-1
df4["Total_Revenue"] = df4["Quantity"] * df4["Total_Price"]
print(df4)

# Ex-2
most_ordered = df4["Product"].value_counts()
print(most_ordered)

print(most_ordered.idxmax())

# Ex-3
avg_quantity = df4.groupby("Product")["Quantity"].mean()

print(avg_quantity)

# Ex-4
import matplotlib.pyplot as plt


sales_by_product = df4.groupby('Product')['Total_Revenue'].sum()

# Plot pie chart
plt.figure(figsize=(6,6))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales Distribution by Product")
plt.show()
