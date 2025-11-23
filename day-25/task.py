from turtle import Turtle,Screen
import pandas
screen = Screen()
turtle = Turtle() #this is because of the formation of world map
state = Turtle()  #this turtle is because so that it can move to the state we have correctly guessed
state.hideturtle()
state.penup()
screen.title("U.S States Game")
shape = "blank_states_img.gif"
screen.addshape(shape)
turtle.shape(shape)
with open("50_states.csv","r") as file:
    states_file = pandas.read_csv(file)
guessed_state = []
while len(guessed_state)<50:
    screen_popup = screen.textinput(title = f"{len(guessed_state)}/50", prompt = "Enter the next state").title()
    if screen_popup == "Exit":
        learn_states = [state for state in states_file["state"] if state not in guessed_state]
        # for state in states_file["state"]:
        #     if state not in guessed_state:
        #         learn_states.append(state)

        pandas.DataFrame(learn_states).to_csv("learn_states.csv")
        break


    if screen_popup in states_file["state"].values:
        guessed_state.append(screen_popup)
        state_data = states_file[states_file["state"]==screen_popup]
        state.write(screen_popup)
        state.goto(int(state_data["x"].item()),int(state_data["y"].item()))



#save all the non guessed states into another csv file



