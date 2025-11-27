from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    my_window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    my_label.config(text = "Timer",fg  ="#9bdeac")
    right_mark.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60

    if reps % 8 == 0:
        countdown(long_break_sec)
        my_label.config(text = " Break",fg = "#e7305b")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        my_label.config(text=" Break", fg="#e2979c")
    else:
        countdown(work_sec)
        my_label.config(text="Session", fg="#9bdeac",font = ("Courier",35))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min_count = math.floor(count/60)
    sec_count = count%60
    if sec_count <= 9:
        sec_count = f"0{sec_count}"   #this is called dynamic typing if we change the data type of something
    canvas.itemconfig(timer_text,text = f"{min_count}:{sec_count}")
    if count >0:
        global timer
        timer = my_window.after(1000,countdown,count -1)
    else:
        start_timer()
        marks =""
        for i in range(math.floor(reps/2)):
            marks += "✔"
        right_mark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #

my_window = Tk()
my_window.title("Pomodoro")
my_window.config(padx = 100,pady = 100,bg =  "#f7f5dd")

#Adding timer label
my_label = Label(text = "Timer",fg = "#9bdeac",bg ="#f7f5dd",font = ("Courier",50))
my_label.grid(column = 1,row =0)

#adding tomato image and typing on it
canvas = Canvas(width = 200,height = 224,bg =  "#f7f5dd",highlightthickness = 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_image)
timer_text  = canvas.create_text(100,130,text = "00:00",fill= "white",font = ("Courier",35,"bold"))
canvas.grid(column =1,row =1 )

#adding start button
start_button = Button(text = "Start",font = ("Courier",15,"bold"),highlightthickness = 0,command = start_timer)
start_button.grid(column = 0,row =2)
#adding end button
reset_button = Button(text = "Reset",font = ("Courier",15,"bold"),highlightthickness = 0,command = reset_timer)
reset_button.grid(column =2,row =2)

#adding right mark
right_mark = Label(text ="",fg ="#9bdeac",bg = "#f7f5dd",font = ("Courier",14,"bold") )
right_mark.grid(column =1,row =3)

my_window.mainloop()