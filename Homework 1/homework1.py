shirt=1250
t_shirt=750
shoes=2560
punjabi=1850

shirt_total=3*shirt
tshirt_total=2*t_shirt
grand_total= shirt_total+tshirt_total+shoes+punjabi
discount_amount=grand_total*0.03
discount_price=grand_total-discount_amount


print("Total price of the shirts is: ",shirt_total)

print("Total price of the t-shirts is: ",tshirt_total)

print("Total price without shoes is: ", shirt_total+tshirt_total+punjabi)

print("Grand total of all products is: ",grand_total)

print("The discount amount is: ", discount_amount)

print(" The payable amount is: ",discount_price)