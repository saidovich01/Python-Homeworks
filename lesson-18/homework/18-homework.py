# Homework 2
import pandas as pd

tackoverflow = pd.read_csv("tackoverflow_qa.csv")

# Ex-1
print(tackoverflow["creationdate"] > "2014-01-01")

# # Ex-2
print(tackoverflow["score"] > 50)

# # Ex-3
print((tackoverflow["score"] > 50) | (tackoverflow["score"] < 100))

# # Ex-4
print(tackoverflow["ans_name"] == "Scott Boston")

# Ex-6
con1 = tackoverflow["ans_name"] == "unutbu"
con2 = tackoverflow["score"] < 50
con3 = (tackoverflow["creationdate"] > "2014-03-01") | (tackoverflow["creationdate"] < "2014-10-01")

final_con = con1 & con2 & con3

print(tackoverflow.loc[final_con])

# Ex- 7
con1 = (tackoverflow["score"] > 5) & (tackoverflow["score"] < 10)
con2 = tackoverflow["viewcount"] > 10000
final_con = con1 | con2

print(tackoverflow.loc[final_con])

# Ex-8
con = tackoverflow["ans_name"] != "Scott Boston"

print(tackoverflow.loc[con, "ans_name"])




#####################################################################################################


# Homework-3
import pandas as pd

titanic_df = pd.read_csv("titanic.csv")

print(titanic_df.head())

# Ex-1
con1 = titanic_df["Sex"] == "female"
con2 = titanic_df["Pclass"] == 1
con3 = (titanic_df["Age"] > 20) & (titanic_df["Age"] < 30)
final_con = con1 & con2 & con3
columns = ["Sex", "Pclass", "Age"]

new_df = titanic_df.loc[final_con, columns]
print(new_df)


# Ex-2
con = titanic_df["Fare"] > 100

new_df = titanic_df.loc[con, "Fare"]
print(new_df)

# Ex-3
con1 = titanic_df["Survived"] == 0
con2 = titanic_df["SibSp"] == 0
con3 = titanic_df["Parch"] == 0
final_con = con1 & con2 & con3

print(titanic_df[final_con])

# Ex-4
con1 = titanic_df["Embarked"] == "C"
con2 = titanic_df["Fare"] > 50
final_con = con1 & con2
columns = ["Embarked", "Fare"]

new_df = titanic_df.loc[final_con, columns]
print(new_df)


# Ex-5
con1 = titanic_df["SibSp"] >= 1
con2 = titanic_df["Parch"] >= 1

print(titanic_df[con1 & con2])

# Ex-6
con1 = titanic_df["Survived"] == 1
con2 = titanic_df["Age"] <= 15
final_con = con1 & con2
columns = ["Age", "Survived"]

print(titanic_df.loc[con1 & con2, ["Age", "Survived"]])

new_df = titanic_df.loc[final_con, columns]
print(new_df)

# Ex-7
con1 = titanic_df["Cabin"].notna()
con2 = titanic_df["Fare"] > 200

print(titanic_df[con1 & con2])

# Ex-8
con = titanic_df["PassengerId"] % 2 == 1

print(titanic_df[con])

# Ex-9
con = titanic_df["Ticket"].value_counts() == 1

print(titanic_df[con])

# Ex-10
con1 = titanic_df["Pclass"] == 1
con2 = titanic_df["Name"].str.contains("Miss")

print(titanic_df[con1 & con2])
