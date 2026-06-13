class Employee:
    
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        
    def display(self):
        print("\nEmployee:")
        print("Name :", self.name)
        print("Department :", self.department)
        print("Salary :", self.salary)
        

class Manager(Employee):
    def display(self):
        print("\nManger:")
        print("Name :", self.name)
        print("Department :", self.department)
        print("Salary :", self.salary)
        
        

emp1 = Employee("Ajay", "IT", 50000)
emp1.display()
    
    
emp2 = Employee("Raamesh", "BDM", 35000)
emp2.display()
    
    
    
emp3 = Employee("Mohan", "Counsellor", 25000)
emp3.display()


mgr = Manager("Ramesh", "DB", 60000);

mgr.display()