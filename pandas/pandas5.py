import pandas as pd

df = pd.read_csv("employee.csv")

print("\n Filtering Data \n")
print(df)
print("\n")

print("\n IT Employee Only\n")
print(df[df["Department"]=="IT"])
print("\n")


print("\nSalary greater than 50000\n")
print(df[df["Salary"] > 50000])
print("\n")

print("\n IT employees with salary greater than 50000\n")
print(df[(df["Salary"] > 50000) & (df["Department"] == "IT")])