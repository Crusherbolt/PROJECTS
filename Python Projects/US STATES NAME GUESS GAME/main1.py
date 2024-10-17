import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# TO Get Coordinate of the image on turtle
# def get_mouse_click_cor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_cor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct", prompt="What's another state's name?").title()

    if answer_state =="Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()
