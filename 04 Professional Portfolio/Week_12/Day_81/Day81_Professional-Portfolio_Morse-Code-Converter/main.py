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

# mapping characters to morse code
# convert text to morse code text
# GUI - only necessary elements
# no database needed
# direct converting of text
# special characters are changed or not needed

code_dict = {
    "a": "._", "b": "_...", "c": "_._.", "d": "_..", "e": ".", "f": ".._.", "g": "__.", "h": "....", "i": "..",
    "j": ".___", "k": "_._", "l": "._..", "m": "__", "n": "_.", "o": "___", "p": ".__.", "q": "__._", "r": "._.",
    "s": "...", "t": "_", "u": ".._", "v": "..._", "w": ".__", "x": "_.._", "y": "_.__", "z": "__.."
}

print("Morse Code Converter")
print("\nBitte Text eintragen:")
text = "Beispiel"
