from tkinter import *
my_window = Tk()
my_window.title("Mile to Km Convertor")
#my_window.minsize(width = 500,height = 500)
my_window.config(padx = 20, pady =20)

my_input = Entry(width = 10)
my_input.grid(column = 1, row = 0)

miles_label = Label(text = "Miles")
miles_label.grid(column = 2,row = 0)

is_equal_to_label = Label(text = "is equal to")
is_equal_to_label.grid(column = 0,row = 1)
km_result_label = Label(text = "0")
km_result_label.grid(column = 1,row =1)
km_label = Label(text = "km")
km_label.grid(column = 2,row =1)


def calculate():
    km_result_label .config(text = float(my_input.get())*1.609)

calculate_button = Button(text = 'Calculate',command = calculate)
calculate_button.grid(column = 1,row = 3)

my_window.mainloop()