# Text to Morse Code Converter

# It is used to convert normal text, given by the user into morse code
# Codetable from online source

# Todo: Planning and programming
# What's the goal
# What's important
# Which methods are important
# What about UI, ...
# What isn't important
# What should be left out
# When is the project finished
# MVP
# TDD
# Add other characters too (. , : ...)

# mapping characters to morse code
# convert text to morse code text
# GUI - only necessary elements
# no database needed
# direct converting of text
# special characters are changed or not needed

code_dict = {
    "a": "._", "b": "_...", "c": "_._.", "d": "_..", "e": ".", "f": ".._.", "g": "__.", "h": "....", "i": "..",
    "j": ".___", "k": "_._", "l": "._..", "m": "__", "n": "_.", "o": "___", "p": ".__.", "q": "__._", "r": "._.",
    "s": "...", "t": "_", "u": ".._", "v": "..._", "w": ".__", "x": "_.._", "y": "_.__", "z": "__..",
    "1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...", "8": "___..",
    "9": "____.", "0": "_____",
    "ä": ".__._", "ö": "___.", "ü": "..__", "ß": "...__..", "ch": "____",
    ".": "._._._", ",": "__..__", ":": "___...", ";": "_._._.", "?": "..__..", "!": "_._.__",
}

code_sign_dict = {
    "KA": "_._._", "BT": "_..._", "AR": "._._.", "SK": "..._._"
}


def convert_text(normal_text):
    global code_sign_dict, code_dict
    code_text = code_sign_dict["KA"] + " "
    # for char in normal_text -> if ch continue once then change to code_dict["ch"]
    # skip is important for the "ch"
    for i in range(len(normal_text)):
        if normal_text[i].lower() == "c" and normal_text[i + 1].lower() == "h":
            continue
        elif normal_text[i - 1].lower() == "c" and normal_text[i+1].lower() == "h":
            code_text += code_dict["ch"] + " "
            continue
        code_text += code_dict[normal_text[i].lower()] + " "
    code_text += code_sign_dict["SK"]
    return code_text


print("Morse Code Converter")
print("\nBitte Text eintragen:")
text = "Beispiel"
print(convert_text(text))
