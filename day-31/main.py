BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
#----------------Working with data----------------#
try:
    df = pandas.read_csv("to_learn_words.csv")
except FileNotFoundError:
    df = pandas.read_csv("french_words.csv")
to_df = df.to_dict(orient = "records")
print(to_df)
current_card = {}
def word_change():
    global current_card,fliper
    my_window.after_cancel(fliper)
    current_card = random.choice(to_df)
    my_canvas.itemconfig(title_text,text = "French",fill = "black")
    my_canvas.itemconfig(main_text,text = current_card["French"],fill = "black")
    my_canvas.itemconfig(image, image=front_image)
    fliper = my_window.after(3000, flip_card)
def flip_card():
    my_canvas.itemconfig(title_text, text="English",fill = "white")
    my_canvas.itemconfig(main_text, text=current_card["English"],fill = "white")
    my_canvas.itemconfig(image, image =back_image)
def is_known():
    to_df.remove(current_card)
    word_change()
    data = pandas.DataFrame(to_df)
    data.to_csv("to_learn_words.csv",index = False)

my_window = Tk()
my_window.title("Flashy")
my_window.config(padx = 50,pady =50 ,background = BACKGROUND_COLOR)
fliper = my_window.after(3000,flip_card)
my_canvas = Canvas(width = 800,height = 526,background = BACKGROUND_COLOR,highlightthickness =0)
front_image = PhotoImage(file = "card_front.png")
back_image = PhotoImage(file = "card_back.png")
image = my_canvas.create_image(  400,256,image = front_image)
title_text = my_canvas.create_text(400,126,text = "",font = ("Ariel",40,"italic"))
main_text = my_canvas.create_text(400,263,text = "",font = ("Ariel",60,"bold"))
my_canvas.grid(row=0,column =0,columnspan = 2)
wrong_image = PhotoImage(file = "wrong.png")
wrong_button = Button(image = wrong_image,highlightthickness = 0,command = word_change)
wrong_button.grid(row = 1,column =0)
right_image = PhotoImage(file = "right.png")
right_button = Button(image = right_image,highlightthickness = 0,command = is_known)
right_button.grid(row = 1,column =1)
word_change()
my_window.mainloop()
