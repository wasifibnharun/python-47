#class inheritance

#parent class
class Animal:
    def eat(self):
        print("The animal is eating")

#child class
class Cow(Animal):
    def eat(self):
        print("The cow is eating")

cow1=Animal()
cow1.eat()

cow2=Cow()
cow2.eat()