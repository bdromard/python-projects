# Importation de la librairie de GUI Tkinter.
import tkinter

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    # Peut aussi être rédigé ainsi => my_label["text"] = "Button got clicked"

# Création de la fenêtre, en objet de Tkinter.
window = tkinter.Tk()
# Création de label
my_label = tkinter.Label(text="Je suis un label", font=("Arial", 24, "bold"))
# Création de button


my_button = tkinter.Button(text="Click Me", command=button_clicked)


# Création d'entry, pour la gestion des inputs



input = tkinter.Entry()


window.title("Utilisation de GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
# Placement du label et du button dans la GUI.
my_label.grid(column=0, row=0)
my_button.grid(column=1, row=1)
input.grid(column=3, row=3)








# Mainloop, method de base pour faire afficher la fenêtre. A mettre à la fin du code.

window.mainloop()

