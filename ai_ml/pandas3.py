import pandas as pd

students = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, 45, 90, 60]
}

df = pd.DataFrame(students)


print("\n");
print(df);


print("\n");
print(df[df["Marks"]>50]);



print("\n");
print(df[df["Marks"]>=80]);
