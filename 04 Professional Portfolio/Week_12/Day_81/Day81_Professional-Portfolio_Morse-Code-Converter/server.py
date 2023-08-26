from flask import app, render_template, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6dPZnzWlSihBXox7C0sKR6b'


# Todo: small form with input of the text
# output is on another side with button to go back
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
