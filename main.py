import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US States Game")
image = 'state_game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv('state_game/50_states.csv')
all_states = state_data['state'].to_list()
def get_state_coordinates(state_to_find):
    state = state_data[state_data['state'] == state_to_find]
    x,y = state.x,state.y
    return (int(x),int(y))

guessed_states = set()
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state")
    answer = answer.title() if answer else None
    if answer in all_states:
        x,y = get_state_coordinates(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x,y)
        t.write(answer)
        guessed_states.add(answer)
    elif answer == 'Exit' or not answer:
        df = pd.DataFrame([state for state in all_states if state not in guessed_states])
        df.to_csv('state_game/missed_states.csv')
        break
    else:
        break


