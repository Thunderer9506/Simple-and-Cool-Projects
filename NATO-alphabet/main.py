import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    name = list(input("Enter your name: ").upper())
    try:
        con = {nato_dict[letter] for letter in name}
    except KeyError as Key:
        print(f"Sorry, we don't take numbers as input, I think you have mistakenly typed {Key}")
        generate()
    else:
        print(con)

generate()
