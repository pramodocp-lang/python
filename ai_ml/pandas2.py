import pandas as pd

employees = {
    "Name": ["John", "Mary", "David"],
    "Salary": [50000, 60000, 55000],
    "Department": ["IT", "HR", "Finance"],
    "Age": [45, 55, 44]
}

df = pd.DataFrame(employees)

print("\n")
print(df)


print("\n")
print("Salary:\n")
print(df["Salary"])

print("\n")
print(df[["Department", "Age"]])


print("\n")
print(df[df["Salary"] >= 55000])


print("\n")
nm = df[(df["Salary"]>=55000) & (df["Age"] <44)]