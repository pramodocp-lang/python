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






#   2. Multiple Inheritance

#   A class can inherit from more than one parent.