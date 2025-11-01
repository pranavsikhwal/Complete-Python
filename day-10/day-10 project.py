#Todo 1 :Write all the four functions :
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
#Todo 2 :Now make a dictionary having keys as +,-,*,/ and values as functions :
calc = {"+":add,"-":sub,"*":mul,"/":div}
#Todo 3; use the dictionary operations to do the calculations:
def calculator():
    is_calculating = True
    number_1 = float(input("Enter the 1st number : \n"))
    while is_calculating:
        for i in calc:
            print(i)
        operator = input("Enter the operator:")
        number_2 = float(input("Enter the 2nd number : \n"))
        result = calc[operator](number_1, number_2)
        print(f"{number_1} {operator}{number_2} = {result}")
        choice = input(f"Type 'y' to continue with {result} or 'n' for new")
        if choice == "y":
            number_1 = result
        else :
            is_calculating = False
            calculator()
calculator()
