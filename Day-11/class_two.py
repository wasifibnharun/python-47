#assigning player class
class Player:
    
    #using constructor
    def __init__(self,shirt_no,position):
        self.shirt_no=shirt_no
        self.position=position
        print(f"Shirt no is {shirt_no} and position is {position}")

    def shot(self,times):
        print(f"Shots total {times} number of occasions")

messi=Player(10,"Striker")
messi.shot(4)