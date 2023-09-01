from converter import Converter

converter: Converter = Converter()

print("Morse Code Converter")
print("\nPlease type in your text:")
text = "Example"
print(converter.convert_text(text))
text = "thing"
print(converter.convert_text(text))
text = "What a long text."
print(converter.convert_text(text))
