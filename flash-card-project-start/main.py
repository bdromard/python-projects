from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

# Current card
current_card = {}
# List of words to learn
to_learn = {}

# Data
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    french_words_df = pandas.read_csv('./data/french_words.csv')
    to_learn = french_words_df.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(canvas_text_language, text="French", fill="black")
    flash_card.itemconfig(canvas_text_word, text=current_card["French"], fill="black")
    flash_card.itemconfig(flash_card_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(flash_card_img, image=card_back)
    flash_card.itemconfig(canvas_text_language, text="English", fill="white")
    flash_card.itemconfig(canvas_text_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# Window initialization
window = Tk()
window.title("Flashy flash")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Labels and buttons
flash_card = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
flash_card_img = flash_card.create_image(400, 263, image=card_front)
canvas_text_language = flash_card.create_text(400, 100, text="", font=FONT_TITLE)
canvas_text_word = flash_card.create_text(400, 260, text="", font=FONT_WORD)
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)


# Grid settings
flash_card.grid(column=0, row=0, columnspan=2)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()