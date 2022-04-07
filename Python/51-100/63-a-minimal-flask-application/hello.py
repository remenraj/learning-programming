# A minimal Flask application to print "Hello, World!"
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")  # showing the homepage, this is a python decorator
def hello_world():
    """Hello World Flask App"""
    return "Hello, World!"


@app.route("/<name>")
def greet(name):
    """Prints the name in the url"""
    return f"Hello, {name}!"


@app.route("/cheese")
def bye_world():
    """Cheese World"""
    return (
        "<h1 style='text-align: center'>Cheese, World!</h1>"
        "<p>This is a paragraph.</p>"
        "<img src='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png' width=200>"
    )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    """Print Bye!"""
    return "Bye!"


if __name__ == "__main__":

    # set environment variable
    # on mac: $ export FLASK_APP=hello.py
    # on windows:
    #   CMD: C:\path\to\app>set FLASK_APP=hello.py
    #   Powershell: PS C:\path\to\app> $env:FLASK_APP = "hello.py"
    # if you want to run the app in debug mode: $ FLASK_DEBUG=1 flask run

    # run flask app: flask run
    # Alternatively you can use python -m flask: python -m flask run
    # if it is not working try cd into the directory and run: python -m flask run

    # # running the app
    # app.run()

    # running the app in debug mode
    app.run(debug=True)
