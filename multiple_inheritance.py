class User:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name);
        
        
class Mentor():
    def __init__(self, subject):
        self.subject = subject
        
    def show(self):
        print(self.subject)
        
        
class Admin(User, Mentor):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

a = Admin("Rahul", "Python")

print(a.name)
print(a.subject)






#   1. super()
#       super() is used to call the parent class constructor or methods.

#   Why use super()?
#       Avoid duplicate code
#       Reuse parent class logic
#       Easier maintenance

