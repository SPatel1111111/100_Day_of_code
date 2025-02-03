import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# using iterrow() we iterate rows for csv data
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

def generate_phonetics():
    word = input("enter the word:").upper()
    try:
        nato_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry letter in alphabets")
        generate_phonetics()
    else:
        print(nato_list)
        generate_phonetics()


generate_phonetics()
