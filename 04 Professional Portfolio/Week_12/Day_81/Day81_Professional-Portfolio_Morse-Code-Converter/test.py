from converter import Converter

# Todo: testcases and tests
# which cases are needed and which not?!
# are there things to test for other parts?
converter: Converter = Converter()

print("Morse Code Converter")
print("\nPlease type in your text:")
text = "Example"
print(converter.convert_text(text))
text = "thing"
print(converter.convert_text(text))
text = "What a long text."
print(converter.convert_text(text))
