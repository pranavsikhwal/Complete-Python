print("Welcome to the tip calculator!")
bill = float(input("What was the total bill (in rupees)? \n "))
tip = int(input("How much tip would you like to give : 10 ,12 or 15 (in percent) \n "))
people = int(input("How many people to split the bill ? \n "))
sum_bill = bill + (bill * tip/100)
per_person = sum_bill / people
print(f"Each person should pay: {(round(per_person , 2))}rupees ")