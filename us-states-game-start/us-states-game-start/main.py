import csv
import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_guessed = 0


game_on = True
while game_on == True:
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    answer_state = screen.textinput(title=f"{states_guessed}/50 States Correct", prompt="Whats a state?")
    if answer_state == "Exit":
        missing_states = []
        for state in all_states():
            if state not in states_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        states_guessed += 1
        title = turtle.Turtle()
        title.hideturtle()
        title.penup()
        state_data = data[data.state == answer_state]
        title.goto(int(state_data.x), int(state_data.y))
        title.write(answer_state)










screen.exitonclick()
