import pandas as pd

df = pd.read_csv("employee.csv")

print("\n")
print(df)

print("\n")
print("\n Print First 2 Rows:")
print(df.head(2))


print("\n")
print("\n Print Last 2 Rows:")
print(df.tail(2))



print("\n")
print("\n Shape")
print(df.shape)



print("\n")
print("\n Column:")
print(df.columns)


print("\n")
print("\n Info")
print(df.info)


print("\n")
print("\n Name Only")
print(df["Name"])


print("\n")
print("\n Salary >50000")
print(df[df["Salary"] > 50000])



print("\n")
print("\n Name, Salary")
print(df[["Name", "Salary"]])

print("\n")


