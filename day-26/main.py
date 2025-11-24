#List comprehension

# list = [1,2,3,4]
# new_list = [n+1 for n in list]
# print(new_list)
#
# name = "Pranav"
# name_list = [n for n in name]
# print(name_list)
#
# list_2 = [1,2,3,4,5]
# double_list = [n*2 for n in list_2]
#double_list = [n*2 for n in range(1,5)]  #another method which doesnt requires line no 11
# print(double_list)
#

# names = ["Pranav","Ujjawal","Shreyansh","Archit","Apurva","Mohit"]
# short_names = [n for n in names if len(n)<6]   #conditional
# print(short_names)
# all_caps = [n.upper() for n in names]
# print(all_caps)


#dictionary comprehension
# import random
# students = ["Pranav","Ujjawal","Shreyansh","Archit","Apurva","Mohit"]
# student_dict = {
#     student : random.randint(1,100) for student in students
# }
# print(student_dict)
# passed_dict = {
#     student:score for(student,score) in student_dict.items() if score>60
# }
# print(passed_dict)

#using pandas looping in dataframe
import pandas
dict = {
    "name":["Pranav","Ujjawal","Shreyansh"],
    "marks": [40,50,60]
}
dataframe = pandas.DataFrame(dict)
for (index,row) in dataframe.iterrows():
    print(row.marks)