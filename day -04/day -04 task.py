# #random module
import random

random_number = random.randint(1,5)    #returns a value between 1 and 100 both are included
print(random_number)

random_number_0to1 = random.random()  #returs a float between o and 1 where 1 is not included
print(random_number_0to1)

random_float = random.uniform(1,10)    #returns a float value between 1 and 10 and both are included
print(random_float)


#to decide random head and tail

toss_a_coin = random.randint(0,1)
if toss_a_coin == 1:
    print("Heads")
else:
    print("Tails")


#lists

India = ["Mumbai","Delhi","Kerala","kolkata","j&k"]
print(India)
India[-1] = "Rajasthan"
print(India)
print(India[1])
India.extend(["Gujrat"])
print(India)
India.append("Karnataka")
print(India)

#choosing random from list
students = ["Vidisha","Ujjawal","Pratigya","Pranav"]
print(random.choice(students))    #1st option
random_student = random.randint(0,3)
print(students[random_student])   #2nd option
print(len(students))


#nested list
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list4 = [list1,list2,list3]
print(list4)


