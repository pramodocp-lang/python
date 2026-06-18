import pandas as pd

df = pd.read_csv("employee.csv")

print("\n")
print("Orginal Data\n")
print(df)


print("\n")
print("Sort by Salary (Ascecding).\n")
print(df.sort_values("Salary"))


print("\n")
print("Sort by Salry (Descending).\n")
print(df.sort_values("Salary", ascending = False))
