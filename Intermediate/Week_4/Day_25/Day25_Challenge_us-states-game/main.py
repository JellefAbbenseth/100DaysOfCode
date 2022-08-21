import turtle

import numpy
import pandas
from board import Board

data_dict = pandas.read_csv("50_states.csv", delimiter=',').to_dict()
# print(data_dict)
# data = pandas.read_csv("50_states.csv", delimiter=",")
# data_list = data['state'].to_list()
# print(data_list)
# print(type(data_list))


def check_input(state_name):
    data_key = [key for key, value in data_dict['state'].items() if value == state_name]
    if len(data_key) >= 1:
        position = (data_dict['x'][data_key[0]], data_dict['y'][data_key[0]],)
        return position
    else:
        return ""


def save_missing_states(user_known_states):
    csv_data = pandas.read_csv("50_states.csv", delimiter=",")
    state_list = csv_data['state'].to_list()
    missing_states = [i for i in state_list if i not in user_known_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")


def capitalize_letters(message):
    parts = message.split(" ")
    message = ""
    for part in parts:
        cap_letter = part.capitalize()
        message += cap_letter + " "
    return message.rstrip()


game_is_on = True
board = Board()
screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
known_states = []

while game_is_on:
    answer_state = screen.textinput(title=f"{board.count_states}/50 States Correct",
                                    prompt="What's another state's name?").capitalize()
    if " " in answer_state:
        answer_state = capitalize_letters(answer_state)
    elif answer_state == "Exit":
        break
    positions = check_input(answer_state)
    if positions == "":
        continue
    board.write_state(positions, answer_state)
    known_states.append(answer_state)
    if board.count_states >= 50:
        game_is_on = False

if board.count_states >= 50:
    print("Congratulation! You knew all states!")
else:
    print("So sad, you can still learn a bit more.")
    save_missing_states(known_states)
