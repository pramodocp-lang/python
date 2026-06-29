import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 150, 170, 200]

plt.figure(figsize=(8,5))
plt.plot(months, sales, color="red", linestyle="--", marker="o", label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid(True)
plt.legend()

plt.savefig("sales_chart.png")
plt.show()