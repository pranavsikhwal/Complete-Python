#SMTP = Simple Mail Transfer Protocol
# import smtplib
#
# my_email = "p19125771@gmail.com"
# password = "haok wpvo cint bfje"
#
# with smtplib.SMTP("smtp.gmail.com",587) as smtp:
#     smtp.starttls()
#     smtp.login(my_email,password)
#     smtp.sendmail(from_addr = my_email ,to_addrs = "pranavsikhwal@gmail.com",msg = "Subject: Hello \n\n Hope you are fine" )

# import smtplib
#
# with smtplib.SMTP("smtp.gmail.com",587) as second_mail:
#     second_mail.starttls()
#     second_mail.login("p19125771@gmail.com","haok wpvo cint bfje")
#     second_mail.sendmail(from_addr = "p19125771@gmail.com",to_addrs = "pranavsikhwal@gmail.com",msg = "Subject:Regarding labs \n\n Please come on time")
# import datetime
# current_time = datetime.datetime.now()
# date_of_birth = datetime.datetime(2004,2,13)
# print(f"Date of birth : {date_of_birth}")
import datetime
import smtplib
import random
with open("quotes.txt")as file:
    file_read = file.readlines()
    file_random =random.choice(file_read)
x = datetime.datetime.now()
if x.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login("p19125771@gmail.com","haok wpvo cint bfje")
        server.sendmail(from_addr = "p19125771@gmail.com",to_addrs = "pranavsikhwal@gmail.com",msg = f"Subject:Good Morning \n\n {file_random}")
