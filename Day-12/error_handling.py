try:
    list=[10,5,0,30]
    result=list[0]/list[1]
    print(result)
    
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("The number you are using is not available")
finally:
    print("Please check the Python manual or visit www.python.org")