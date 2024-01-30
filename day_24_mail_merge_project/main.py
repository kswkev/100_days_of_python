#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

STARTING_LETTER_PATH = "Input/Letters/starting_letter.txt"
NAMES_PATH = "Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend/"
FIELD = "[name]"

with open(STARTING_LETTER_PATH) as template_file:
    template_text = template_file.read()

with open(NAMES_PATH) as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    letter_text = template_text.replace(FIELD, name)
    with open(f"{OUTPUT_PATH}Letter_for_{name}.txt", mode="w") as output_file:
        output_file.write(letter_text)
