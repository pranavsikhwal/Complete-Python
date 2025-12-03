from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain ): #it is the concept of type hint in python where we give a type that what value it should be
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20,pady = 20, bg = "#375362")
        self.score = Label(text = "Score:0",bg =THEME_COLOR ,fg = "white",font =("Arial",20,"italic"))
        self.score.grid(column =1,row =0)
        self.canvas = Canvas(width = 300,height = 250,bg ="white")
        self.question_text = self.canvas.create_text(150,125,width = 280,text = "Quizz",font =("Arial",20,"italic"),fill = "black" )
        self.canvas.grid(column = 0,row =1,columnspan =2,pady = 50)
        self.wrong_image = PhotoImage(file= "./images/false.png")
        self.right_image = PhotoImage(file="./images/true.png")
        self.wrong_button = Button(image = self.wrong_image,highlightthickness = 0,command = self.true_answer)
        self.wrong_button.grid(column =0,row =2)
        self.right_button = Button(image=self.right_image,highlightthickness = 0 ,command = self.false_answer)
        self.right_button.grid(column =1,row =2)
        self.right_button.grid(column =1,row =2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score:{self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = quiz_text)
        else:
            self.canvas.itemconfig(self.question_text,text ="You have reached the maximum number of questions")
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.next_question)


