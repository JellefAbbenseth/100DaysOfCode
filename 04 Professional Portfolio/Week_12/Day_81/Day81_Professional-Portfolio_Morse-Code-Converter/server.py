from flask import app, render_template, Flask

# Text to Morse Code Converter

# It is used to convert normal text, given by the user into morse code
# Codetable from online source for the most important characters.

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6dPZnzWlSihBXox7C0sKR6b'


# Todo: small form with input of the text
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/converted')
def converted():
    return render_template("")


if __name__ == "__main__":
    app.run(debug=True)
