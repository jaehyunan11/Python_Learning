# {new_key:new_value for (key, value) in dict.items()}

import pandas as pd
# TODO1: Create a dictionary in this format:
# {"A":"Alfa", "B":"Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

trial = 0
program_on = True
while program_on:
    # TODO2 : Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    trial += 1
    print(output_list)
    if trial == 2:
        program_on = False



