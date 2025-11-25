# def add_numbers(*args): #This *args allows us to pass as much as argument we want to pass
#     sum = 0
#     for number in args:
#         sum += number
#     return sum
#
# print(add_numbers(12,456,34,23,56))

#lets understand kwargs
def calculation(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    n *= kwargs["Multiply"]
    n += kwargs["Add"]
    n -= kwargs["Subtract"]
    print(n)

calculation(345,Multiply = 5, Add =67,Subtract = 5)