class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.salary=salary
        
    def update_role(self,promotion,new_salary):
        self.role=promotion
        self.salary=new_salary
        
emp1=Employee("John","Assistant manager",90000)
print(f"Hi {emp1.name}!You are currently working as an {emp1.role} and you have a salary of {emp1.salary}")

emp1.update_role("CEO",120000)
print(f"Congratulations,John!You are promoted to {emp1.role} and will be paid with a salary of {emp1.salary}")