hasgoodcreditrecord=True
hashighincome=True
is_criminal=True

if(is_criminal==True and hashighincome==True or hasgoodcreditrecord==True):
    print("Criminal is not allowed to take loan according to bank's constitution")
elif(hashighincome==True and hasgoodcreditrecord==True):
    print("You are eligible for loan")
else:
    print("Bank authority will refuse the loan")