from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_data():
    username = request.form['username']
    mail = request.form['email']
    phone_number = request.form['phoneNumber']
    message = request.form['message']
    print(f"""
        Username: {username}
        E-Mail: {mail}
        Phone number: {phone_number}
        Message: {message}        
    """)
    return f"<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
