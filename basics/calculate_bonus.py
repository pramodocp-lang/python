def calculate_bonus(salary):
    if salary > 50000:
        return salary * 0.10
    elif salary > 30000:
        return salary * 0.05
    else:
        return salary * 0.02

salary = int(input("Enter Salary: "))

bonus = calculate_bonus(salary)

print("Bonus =", bonus)


This is the common content.

Added to all files.



