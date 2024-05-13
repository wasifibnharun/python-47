class Student:
    def __init__(self,name,class_no):
        self.name=name
        self.class_no=class_no

me=Student("Wasif",11)
print(f"You are {me.name} and this is class number {me.class_no}")