import turtle
import pandas

# Initializes screen, with title and map as image.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Gets data from .csv file and puts it into a list.
data = pandas.read_csv("50_states.csv")
all_states_list = data.state.to_list()

# List where to put guessed states by player.
guessed_states = []

# While loop to initiate the game.
while len(guessed_states) < 50:
    # Prompt that gets player's input.
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Exit state, and that creates a .csv file with missed states by the player.
    if answer_state == "Exit":
        missed_states = [state for state in all_states_list if state not in guessed_states]
        missed_states_as_df = pandas.DataFrame(missed_states)
        missed_states_as_df.to_csv()
        break
    # If correct guess by the player, puts state's name on the map with coordinates from .csv file.
    if answer_state in all_states_list:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

