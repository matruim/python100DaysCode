import pandas

# {"A": "Alfa", "B": "Bravo"}
csv = pandas.read_csv("nato_phonetic_alphabet.csv")
natoAlpha = {row.letter: row.code for (index, row) in csv.iterrows()}

userWord = input("Word to convert to Nato Alphabet: ")
result = [natoAlpha[letter] for letter in userWord.upper()]
print(result)
