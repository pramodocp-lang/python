a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

class User:
    def __init__(self, name):
        self.name = name

class Mentor(User):
    def __init__(self, name, subject):
        super().__init__(name)   # Call parent constructor
        self.subject = subject

m = Mentor("Rahul", "Python")

print(m.name)
print(m.subject)






#   1. super()
#       super() is used to call the parent class constructor or methods.

#   Why use super()?
#       Avoid duplicate code
#       Reuse parent class logic
#       Easier maintenance

