# Email and Password login using WTForms
# WTForms documentation: https://wtforms.readthedocs.io/en/2.3.x/crash_course/
# WTForms validators documentation: https://wtforms.readthedocs.io/en/2.3.x/validators/#module-wtforms.validators
# How Forms get data: https://wtforms.readthedocs.io/en/2.3.x/crash_course/#how-forms-get-data
# Flask Bootstrap Documentation: https://pythonhosted.org/Flask-Bootstrap/basic-usage.html


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap, url_for


class LoginForm(FlaskForm):
    """ Login Form """
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])  
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "sadjfoaefifniasdfnaisfeniwef" # some random string
Bootstrap(app=app)


@app.route("/")
def home():
    """ Home page """
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Login page """
    login_form = LoginForm() # create an instance of the form
    login_form.validate_on_submit() # validate_on_submit() returns True if the form is valid, False otherwise.
    
    # # printing the email entered
    # if login_form.validate_on_submit():
    #     print(login_form.email.data)

    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
        

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)