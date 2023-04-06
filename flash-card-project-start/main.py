from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")


# Data
french_words_df = pandas.read_csv('./data/french_words.csv')
select_french_row = french_words_df['French']

def generate_word():
    random_word = french_words_df.at[random.randint(2, 102), "French"]
    return random_word

# Randomize word function on click
def change_word():
    flash_card.itemconfigure(canvas_text_word, text=generate_word())


# Window initialization
window = Tk()
window.title("Flashy flash")

# Labels and buttons
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flash_card = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
flash_card.create_image(400, 263, image=card_front)
canvas_text_language = flash_card.create_text(400, 100, text="French", font=FONT_TITLE)
canvas_text_word = flash_card.create_text(400, 260, text=generate_word(), font=FONT_WORD)
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=change_word)
wrong_button = Button(image=wrong_image, highlightthickness=0)


# Grid settings
flash_card.grid(columnspan=2)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

window.mainloop()