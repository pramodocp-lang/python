name = input("Enter Name of the Employee:")

salary = int(input("Enter Salary:"))

hra = round(salary * 30/ 100, 2)

bonus = round(salary * 5/ 100 , 2)

print("\nEmployee Name  :",  name)
print("\nBasic Salary   :",  salary)
print("\nHRA            :",  hra)
print("\nBonus          :",  bonus)
print("\nGross Salary   :",  round(salary + hra + bonus, 2))



