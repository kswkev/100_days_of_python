import pandas
CSV_FILE = "nato_phonetic_alphabet.csv"
PROMPT = "Please enter a word to be converted into NATO phonetic: "

#Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.read_csv(CSV_FILE)
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.

user_input = input(PROMPT).upper()
nato_output = [nato_dict[character] for character in user_input if character in nato_dict]
print(user_input)
print(nato_output)