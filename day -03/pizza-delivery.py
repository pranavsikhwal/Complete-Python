print("Welcome to python pizza delivery")
size = input("What size pizza do you want? (S/M & L) \n")
pepperoni = input("Do you want pepperoni? (Y/N) \n")
extra_cheese = input("Do you want extra cheese? (Y/N) \n")
price = 0
if size == "S":
    price = 100
elif size == "M":
    price = 135
elif size == "L":
    price = 200

if pepperoni == "Y":
    if size == "S":
        price += 20
    else:
        price += 30
if extra_cheese == "Y":
    price += 10
print(f"Your final bill is {price}")