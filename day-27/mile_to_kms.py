import tkinter

window = tkinter.Tk()
window.title("Convertissseur de miles en kilomètres")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)


def convert_miles_to_kms():
    miles = float(mile_input.get())
    kilometers = miles * 1.609
    result_label.config(text=f"{kilometers}")


# Input for miles
mile_input = tkinter.Entry(width=7)


# Label for miles
mile_label = tkinter.Label(text="Miles")


# Calculate button
calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_kms)

# Result label
is_equal_label = tkinter.Label(text="is equal to")
result_label = tkinter.Label(text="0")
kilometers_label = tkinter.Label(text="Km")

# Positioning of components
mile_input.grid(column=1, row=0)
mile_label.grid(column=2, row=0)
calculate_button.grid(column=1, row=2)
is_equal_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
kilometers_label.grid(column=2, row=1)


window.mainloop()