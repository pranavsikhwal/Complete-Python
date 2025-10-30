is_continue = True
name_bid_dictionary = {}
while  is_continue:
    name = input("Enter your name: \n")
    bid_price = int(input("Enter your bid price : \n"))
    name_bid_dictionary[name]=bid_price
    other = input("Are there any other user who want to bid (yes/no) \n").lower()
    if other == "yes":
        is_continue = True
    else :
        is_continue = False
highest = max(name_bid_dictionary,key = name_bid_dictionary.get)
print(f"{highest} is the person having highest bid and it is {max(name_bid_dictionary.values())}")
