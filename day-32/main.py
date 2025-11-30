##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a random letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
#----------Let's Start---------#
import datetime
import pandas
import random
import smtplib

#-------importing all these three letters----------#
name = "[NAME]"
with open("letter_1.txt")as file:
    file_1 = file.read()
    # print(file_1)

with open("letter_2.txt") as file:
    file_2 = file.read()
    # print(file_2)
with open("letter_3.txt") as file:
    file_3 = file.read()
    # print(file_3)

replace_1 = file_1.replace(name,"Pranav")
replace_2 = file_2.replace(name,"Pranav")
replace_3 = file_3.replace(name,"Pranav")
replace_list = [replace_1,replace_2,replace_3]
random_choice = random.randint(0,2)
choice_in_mail = replace_list[random_choice]
# print(choice_in_mail)


#-------------dealing with date------------#
birth_date = datetime.datetime.now()
birthdate = (birth_date.month,birth_date.day)   #because month and day are attribute
# print(birthdate)    #we have created this as a tuple because we need this in dictionary below and dictionary treat tuple as a key we cant use dictionary because tuple and key both are im mutable

birthday = pandas.read_csv("birthdays.csv")
# print(birthday)

#let create dictionary
birthday_dict = {
    birthdate : birthday_row for (index,birthday_row) in birthday.iterrows()
}
# print(birthday_dict)
if birthdate in birthday_dict:
    #lets now create email
    with smtplib.SMTP("smtp.gmail.com",587) as birthday_mail:
        birthday_mail.starttls()
        birthday_mail.login("p19125771@gmail.com","haok wpvo cint bfje")
        birthday_mail.sendmail(from_addr = "p19125771@gmail.com",to_addrs = "pranavsikhwal@gmail.com",msg = f"Subject:Happy Birthday!\n\n {choice_in_mail}")


#later set it automatically on python anywhere