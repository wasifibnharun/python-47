command=""
started=False

while True:
    command=input(">>>")
    if command=="start":
        if started==True:
            print("Car is already started")
        else:
            started=True
            print("Car Started")
    elif command=="stop":
        if not started==True:
            print("Car is already stopped..")
        else:
            started=False
            print("Car has stopped")
    elif command=="help":
        print('''start: To start the car
                 stop: To stop the car
                 quit: To quit the game
              ''')    
    elif command=="quit":
        break
    else:
        print("Unknown command")