class Employee:
    
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        
    def display(self):
        print("Name :", self.name)
        print("Department :", self.department)
        print("Salary :", self.salary)
        
emp1 = Employee("Ajay", "IT", 50000)
emp1.display()
    
    
emp2 = Employee("Raamesh", "BDM", 35000)
emp2.display()
    
    
    
emp3 = Employee("Mohan", "Counsellor", 25000)
emp3.display()