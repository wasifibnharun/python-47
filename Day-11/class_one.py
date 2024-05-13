#creating a class
class Room:
    #properties declaration
    length=0
    width=0

    #defining a function or method
    def calculate_area(self):
        print("Area of room is:",self.length*self.width)


# creating object from room class
# drawing_room=Room()

# assigning values
# drawing_room.length=20
# drawing_room.width=15

# accesing the method
# drawing_room.calculate_area()

bedroom=Room()
bedroom.length=15
bedroom.width=10
bedroom.calculate_area()