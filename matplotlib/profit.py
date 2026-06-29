import numpy as np
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales = [100,120,140,160]
profit = [20,30,40,45]

x = np.arange(len(months))
width = 0.35

plt.bar(
    x - width/2,
    sales,
    width,
    label="Sales"
)

plt.bar(
    x + width/2,
    profit,
    width,
    label="Profit"
)

plt.xticks(x, months)

plt.legend()

plt.show()