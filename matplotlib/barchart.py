import matplotlib.pyplot as plt

departments = ["HR", "IT", "Sales", "Finance" "Total"]
employees = [15, 40, 30, 20]
colors = ["red", "blue", "green", "orange"]


bars = plt.bar(departments, employees, color=colors, width=0.3)


for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )
    
    
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()