print("Ram"[0])
print("Computer"[-1])
print("Computer"[-2])
print("Computer"[-3])

print("123"+"456")    #it will work as string and join this
print(int("123")+int("456"))  #this will convert the data type of this into integer
print(123+456)        #it adds because it is considering them as numbers

print(1.345)          #float value
print(True,False)    #boolean value

print(type(True))          #this type function gives the data type .
print(type(123))
print(type(12.345))
print(type("python"))

# print(len(12345))   not valid because this length doesnt works with integer
print(len("12345"))   #convert it in string

#print("No of letters in your name :" + len(input("Enter your name : ")))   This will throw an error because we can't add different data types
no = len(input("What is your name? \n"))
print("No of letters in your name :" + str(no))

#mathematical operations
print(3+4)
print(3**4)
print(3//4)
print(3/4)
print(3*4)
print(int(3/4))
print(round(3/4))  #if greater than .5 round to next big digit else same digit
print(round(3/4 ,2))


#f-string
#to add different data types we use f-string
age = 18
is_passed = True
print(f"Age of person is {age} . Did he cleared driving licence test : {is_passed}")

