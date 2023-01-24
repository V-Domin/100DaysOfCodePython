import turtle
from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
state = Turtle()
screen.title('USA Game')

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
game_is_on = True



data = pd.read_csv('50_states.csv')

score = 0
correct_score = 0
list_states = data.state.to_list()
guessed_states_list = []

while game_is_on:
    user_guess = turtle.textinput(f"{score}/50 Guess USA states", "What's the next state?").title()
    user_state = data[data.state == user_guess]
    if user_guess in list_states:
        guessed_states_list.append(user_guess)
        x_coor = user_state.x
        y_coor = user_state.y
        state.penup()
        state.goto(int(x_coor), int(y_coor))
        state.write(f"{user_guess}")
        score += 1
        correct_score += 1

    elif user_guess == 'Exit' or score == 50:
        missing_state = [state for state in list_states if state not in guessed_states_list]


        # for state in list_states:
        #     if state not in guessed_states_list:
        #         missing_state.append(state)


        df = pd.DataFrame(missing_state)
        df.to_csv('states_to_learn.csv')
        print(f"Game Over. Your score: {correct_score}/50")
        game_is_on = False

    else:
        score += 1
        continue




