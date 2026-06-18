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