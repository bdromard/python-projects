from tkinter import *
from tkinter import messagebox
import random
# Library to manage automatic copy / pasting
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generates a randomized password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = []
    password_numbers = []
    password_symbols = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    random_password = "".join(password_list)

    # Inserts randomized password into password input, and copies it in the clipboard.
    password_input.insert(0, f'{random_password}')
    pyperclip.copy(f'{random_password}')
# ---------------------------- SAVE PASSWORD ------------------------------- #
save_file = open("data.txt", "a")

# Function that opens data.txt, takes every input and saves them in it, then removes website and
# password inputs.
def save_data():
    website = website_input.get()
    email = email_input.get()
    password = generate_password()

    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n "
                                                  f"Password : {password}. Is it OK to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f'\n{website} | {email} | {password}')
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window config
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas config with logo
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

# Labels, buttons and inputs
website_label = Label(text="Website:")
website_input = Entry(width=35)
# Method that focuses input on this entry
website_input.focus()
email_label = Label(text="Email/Username:")
email_input = Entry(width=35)
email_input.insert(END, "benjamin@email.com")
password_label = Label(text="Password:")
password_input = Entry(width=16)
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
add_button = Button(text="Add", width=32, command=save_data)

website_label.grid(column=0, row=1)
website_input.grid(column=1, columnspan=2, row=1)
email_label.grid(column=0, row=2)
email_input.grid(column=1, columnspan=2, row=2)
password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, columnspan=2, row=4)
canvas.grid(column=1, row=0)


window.mainloop()