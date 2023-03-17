PLACEHOLDER = "[name]"
class Letter:

    def __init__(self, name):
        with open("./Input/Letters/starting_letter.txt", mode="r") as text_letter:
            text_to_read = text_letter.read()
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as letter_for_guest:
            letter_for_guest.write(text_to_read)
        with open("./Input/Letters/starting_letter.txt", mode="r") as new_letter:
            text_to_modify = new_letter.read()
            final_text = text_to_modify.replace(PLACEHOLDER, f"{name.strip()}")
            self.text = final_text




