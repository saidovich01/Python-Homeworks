# Task-1
import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40], 
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

print(df)

# Ex-1
col_map = {
    "First Name": "first_name",
    "Age": "age" 
}

new_df = df.rename(columns=col_map)
print(new_df)

# Ex-2
print(df.head(3))

# Ex-3
individuals = df["Age"]
print(individuals.mean())

# Ex-4
print(df[["First Name", "City"]])

# Ex-5
salary_df = df.assign(Salary=np.random.randint(50000, 150001, size=len(df)))
print(salary_df)

# Ex-6
print(salary_df.describe())


##################################################################################################

# Task-2
import pandas as pd

# Ex-1

data = {
    "Month" : ["Jan", "Feb", "Mar", "Apr"],
    "Sales" : [5000, 6000, 7500, 8000],
    "Expenses" : [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

print(sales_and_expenses)

# Ex-2
print(f"Max Sale: {sales_and_expenses['Sales'].max()}\nMax expenses: {sales_and_expenses['Expenses'].max()}")

# Ex-3
print(f"Min Sale: {sales_and_expenses['Sales'].min()}\nMin expenses: {sales_and_expenses['Expenses'].min()}")


# Ex-4
print(f"Avg Sale: {sales_and_expenses['Sales'].mean()}\nAvg expenses: {sales_and_expenses['Expenses'].mean()}")


#########################################################################################################################


# Task-3
import pandas as pd 

# Ex-1
data = {
    "Category" : ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January" : [1200, 200, 300, 150],
    "February" : [1300, 220, 320, 160],
    "March" : [1400, 240, 330, 170],
    "April" : [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Ex-2
print(expenses.set_index('Category').max())

# Ex-3
print(expenses.set_index('Category').min())

# Ex-4
print(expenses.set_index('Category').mean())

