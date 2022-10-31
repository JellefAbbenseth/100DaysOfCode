import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(f"{key}: {value}")


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alphabet_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ")
phonetic_word = \
    [nato_alphabet_dict[letter.upper()] for letter in user_word if letter.upper() in nato_alphabet_dict]
print(phonetic_word)
