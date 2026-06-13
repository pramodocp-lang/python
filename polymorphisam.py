class Employee:
    
    def display(self):
        print("\nEmployee:")
        

class Manager():
    def display(self):
        print("\nManger:")
        
        
users = [Employee(), Manager()]

for user in users:
    user.display()