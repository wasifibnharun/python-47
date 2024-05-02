i=0

while i<3:

    username=input("username: ")
    password=input("password: ")
    if username=="admin" and password=="admin":
        print("Welcome")
        break
    else:
        print("Incorrect username or password")
        i+=1
        continue
else:
    print("The system has been locked")
