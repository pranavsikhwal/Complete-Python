#Tkinter is simply Python’s built-in toolkit for making GUI apps — little windows with buttons, text boxes, dropdowns, and all the everyday widgets that make programs feel alive instead of just staring at a terminal.
import tkinter
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500,height = 300)
window.config(padx = 100,pady =200)
#dealing with label
label = tkinter.Label(text = "I am a label just place me anywhere you want inside his window", font = ("Arial",24,"bold"))
label.grid(column = 0, row = 0)
#label["text"] = "New Text"
label.config(text = "New Text")
#dealing with button
def button_clicked():
    text_input = input.get()
    #label.config(text = "Button got clicked")
    label.config(text = input.get())
button = tkinter.Button(text = "Click me",command = button_clicked)
button.grid(column = 1,row =1)
new_button = tkinter.Button(text = "Click me after 1st button")
new_button.grid(column = 2, row =0)
#Entry
input = tkinter.Entry(width = 10)
input.grid(column = 3,row = 3) #there are 3 ways pack , place and grid








window.mainloop()