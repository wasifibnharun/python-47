number=float(input("Enter your obtained marks: "))

if number>=90 and number<=100:
    print("Congrats,you have got A+")
elif number>=80:
    print("You have got A grade")
elif number>=70:
    print("You have got A- grade")
elif number>=60:
    print("You have got B grade")
elif number>=50:
    print("You have got C grade")
elif number>=40:
    print("You have got D grade")
else:
    print("You have failed the test")