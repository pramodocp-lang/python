try:
    age = int(input("Enter Age: "))
    print("Your Age is", age)

except ValueError:
    print("Invalid Input. Please enter a number.")