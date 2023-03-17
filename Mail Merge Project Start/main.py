#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


from letter import Letter

with open("./Input/Names/invited_names.txt", mode="r") as guests:
    text_letter = guests.readlines()
    number_of_guests = len(text_letter)

for x in range(number_of_guests):
    x = Letter(text_letter[x])
    
