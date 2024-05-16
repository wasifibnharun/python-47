class Employee:
    def __init__(self,name,post,salary):
        self.name=name
        self.post=post
        self.salary=salary

    def daily_task(self,task_name):
        print(f"He is doing {task_name}")

class Manager(Employee):
    def daily_task(self, task_name):
        print(f"He is managing his {task_name}")

emp1=Employee("Wasif","CEO",20000000)
print(f"Welcome {emp1.name},you are now promoted to our official {emp1.post} and you are getting a salary of {emp1.salary}")
emp1.daily_task("Management")

manager1=Manager("Prithiraj Boshak","CEO",49900)
print(f"The new manager is {manager1.name} and his designation is {manager1.post}")
manager1.daily_task("communication to executives")