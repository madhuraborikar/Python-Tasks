# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit


cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost_price:
    print("It's a profit.")
else:
    print("It's a loss")