class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        super().display()
        print(self.department)
emp=Employee('abcd',12000)
emp.display()
Mgr=Manager('efghi',15000,'logistics')
Mgr.display()


