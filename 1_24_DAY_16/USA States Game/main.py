import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("USA States Game")
# screen.screensize(600,600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
state_list = df.state.to_list()
guessed_states =[]

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State correct",prompt="what's the another state name??").title()

    if answer_state == "Exit":
        missing_state =[state for state in state_list if state not in guessed_states]
        # missing_state=[]
        # for state in state_list:
        #     if state not in guessed_states :
        #         missing_state.append(state)
        new_state=pd.DataFrame(missing_state)
        new_state.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


