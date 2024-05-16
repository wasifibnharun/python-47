import functions
qty=float(input("Enter the quantity: "))
price=float(input("Enter the price of the clothes: "))

total_price=qty*price
print("The total price is",total_price)
functions.discount(total_price)
functions.payment(total_price)