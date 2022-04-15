# simple html form example
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    """ Receive data from the form and displays it"""
    name = request.form.get("username")
    password = request.form.get("password")
    return f"<h1>Name: {name}</h1>"\
        f"Password: {password}"

if __name__ == "__main__":
    app.run(debug=True)