import numpy as np

print()
print("Sales Analysis")
print()
sales = np.array([
    12000,
    18000,
    22000,
    16000,
    25000,
    30000,
    27000
])


print("Sales Data")
print(sales)
print()



print("Total:")
print(sales.sum())
print()



print("Average:")
print(sales.mean())
print()



print("Max:")
print(sales.max())
print()



print("Min:")
print(sales.min())
print()




print("Above > 20,000:")
print(sales[sales >20000])
print()



print("Below < 20,000:")
print(sales[sales <20000])
print()



print("Increase 15%:")
print(sales * 0.15 + sales)
print()



print("Increasing Order:")
print(np.sort(sales))
print()



print("Index of Max Salary:")
print(np.argmax(sales))
print()




print("Save to file sales.npy:")
print(np.save("sales.npy", sales))
print()



print("Load from file sales.npy:")
print(np.load("sales.npy"))
print()


