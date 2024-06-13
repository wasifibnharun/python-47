def discount(t_price):
    disc1=t_price-(t_price*0.10)
    print(f"You are given 10% discount and the payable price is {disc1}")
    
def payment(tot_price):
    payment_method=input("By which medium are you wanting to pay?\n")
    if  payment_method=="Bkash":
        price=tot_price*.05
        print(f"Congratulations,you got a cashback of {price} tk")
    elif payment_method=="Nagad":
        price=tot_price*.03
        print(f"Congratulations,you got a cashback of {price} tk")
    elif payment_method=="Rocket":
        price=tot_price*.04
        print(f"Congratulations,you got a cashback of {price} tk")
    else:
        print(f"Sorry,we don't have any cashback for {payment_method} payment")