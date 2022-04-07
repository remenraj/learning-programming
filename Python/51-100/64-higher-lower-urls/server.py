# Flask app running higher lower url game
# Guess the random number between 0 and 9, and enter it in the url (e.g. 127.0.0.1:5000/7), to see if you win.

from flask import Flask
import random

app = Flask(__name__)

# generating a random number
random_number = random.randint(0, 9)
     

def lower():
    return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
     
     
def winner():
    return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


def higher():
    return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>" 
     
     
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9 </h1>"\
                "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"\
                    f"{random_number}"
                    
               
@app.route("/<guess>")
def check_number(guess):
    # checking if the guess is correct
    if int(guess) == random_number:
        return winner()
    elif int(guess) < random_number:
        return lower()
    else:
        return higher()
    


# running the app
if __name__ == "__main__":
    app.run(debug=True)