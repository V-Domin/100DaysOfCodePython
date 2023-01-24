import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic = [dictionary[letter] for letter in word]
        print(phonetic)
    except KeyError:
        print("Sorry, only letter in the alphabet please")
        generate_phonetic()



generate_phonetic()