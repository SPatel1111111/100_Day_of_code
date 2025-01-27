import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
# print(data.to_dict())
#using iterrow() we iterate rows for csv data
data_dict={row.letter:row.code for (index,row) in data.iterrows()}
print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word =input("enter the word:").upper()
nato_list=[data_dict[letter] for letter in word]
print(nato_list)
