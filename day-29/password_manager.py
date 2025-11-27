from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_list =( [random.choice(letters) for _ in range(random.randint(8, 10))] +[random.choice(symbols) for _ in range(random.randint(2, 4))] +[random.choice(numbers) for _ in range(random.randint(2, 4)) ])

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def file():
    get_website = website_entry.get()
    get_email = email_entry.get()
    get_password = password_entry.get()
    get_info = {
        get_website :{
            "Email" : get_email,
            "Password": get_password}
    }

    if len(get_website) == 0 or len(get_password) == 0:
        messagebox.showerror(title = "Error" ,message= "Error! Please enter all details")
    else:
        is_ok = messagebox.askokcancel(title = get_website,message = f"The password you entered for {get_website} is {get_password} .If you are sure than proceed .")
        if is_ok :
            try:
                with open("saved_data.json" ,mode = "r") as File :
                    data = json.load(File)  #reading the json file

            except:
                with open("saved_data.json", mode="w") as File:
                    json.dump(get_info, File, indent=4)  # writing in json file the updated data

            else:
                data.update(get_info)  #updating the json file
                with open("saved_data.json", mode="w") as File:
                    json.dump(data,File,indent =4)   #writing in json file the updated data
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- Find Password ---------------------------------#
def search():
    website = website_entry.get()
    try:
        with open("saved_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title = "Error",message = "File not found")
    else:
        if website in data:
            messagebox.showinfo(title = website_entry.get(),message = f"Email : {data[website]["Email"]} \n Password :{data[website]["Password"]}")
        else:
            messagebox.showinfo(title ="Error", message = "No records found")

# ---------------------------- UI SETUP ---------------------------------#

my_window = Tk()
my_window.title( "Password Manager")
my_window.config(padx = 20,pady = 20)

canvas = Canvas(width = 200,height = 200)
my_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = my_image)
canvas.grid(column = 1,row =0)

website_label = Label(text = "Website:")
website_label.grid(column =0,row =1)

website_entry = Entry(width =21)
website_entry.grid(column =1,row =1)
website_entry.focus()

email_label = Label(text = "Email/Username:")
email_label.grid(column = 0,row =2)

email_entry = Entry(width =35)
email_entry.grid(column = 1,row = 2,columnspan = 2)
email_entry.insert(0,"pranavsikhwal@gmail.com")

password_label = Label(text = "Password:")
password_label.grid(column =0,row = 3)

password_entry = Entry(width =21)
password_entry.grid(column =1,row =3)

password_button = Button(text = "Generate Password",command = generate_password)
password_button.grid(column = 2,row = 3)



add_button = Button(text = "Add",width =35,command = file)
add_button.grid(column =1,row = 4,columnspan =2)

search_button = Button(text = "Search",command = search)
search_button.grid(column = 2,row =1)

my_window.mainloop()