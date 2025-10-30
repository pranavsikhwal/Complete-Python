#functions in python
# def name():
#     print("hello ")
#     print("I am Pranav")
#     print("Currently learing python")
#
# name()
# functions with input
def name_input(name):
    print("Hello")
    print(f"I am {name}")
    print("Currently learing python")
name_input("Pranav")
#functions with multiple input
def random(name,age):
    print(f"Hello  My name is {name}")
    print(f"My age is {age}")

random(age = "Pranav", name = 20) #keyword agrument
random("Pranav", 20) #Positional agrument
