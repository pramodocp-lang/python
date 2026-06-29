import matplotlib.pyplot as plt

departments = [
    "HR",
    "IT",
    "Sales",
    "Finance",
    "Marketing"
]

employees = [
    15,
    40,
    30,
    20,
    18
]

plt.figure(figsize=(8,5))

plt.bar(
    departments,
    employees,
    color="steelblue"
)

plt.title("Employee Distribution")

plt.xlabel("Departments")

plt.ylabel("Employees")

plt.grid(axis="y")

plt.show()