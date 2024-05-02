command=""
started=False

while True:
    command=input("Enter a command> ")
    if command=="start":
        if started:
            print("The car is already started")
        else:
            started=True
            print("Car has started now")
    elif command=="stop":
        if not started:
            print("Car is already stopped")
        else:
            started=False
            print("Car has stopped now")
    elif command=="help":
        print('''  
start: To start the car
stop: To stop the car
quit: To quit the game
              ''')
    elif command=="quit":
        break
    else:
        print("Error!Unknown command")