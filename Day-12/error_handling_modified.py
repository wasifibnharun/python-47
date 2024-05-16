try:
    list=[10,5,0,30]
    result=list[0]/list[1]
    print(result)
    
except (ZeroDivisionError,IndexError,TypeError,NameError):
    print("Please check your input")
finally:
    print("Please check the Python manual or visit www.python.org")