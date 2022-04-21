# Flask-Bootstrap: https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#examples
# Bootstrap Tables: https://getbootstrap.com/docs/4.5/content/tables/
# WTForms Validators: https://wtforms.readthedocs.io/en/2.3.x/validators/

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6do45nzWlSihBXox7C0sKR6b"
Bootstrap(app)


# cafe csv file directory
try:
    CAFE_DATA_FILE_DIR = (
        r"learning-programming\Python\51-100\72-coffee-and-wifi-website\cafe-data.csv"
    )
except FileNotFoundError:
    print("Cafe data file not found")


class CafeForm(FlaskForm):
    """ Cafe Form Class """
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    cafe_location = StringField(
        "Cafe Location on Google Maps(URL)", validators=[DataRequired(), URL()]
    )
    opening_time = StringField("Opening Time, e.g.: 9 AM", validators=[DataRequired()])
    closing_time = StringField("Closing Time, e.g.: 9 PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired()],
    )
    wifi_strength_rating = SelectField(
        "Wifi Strength Rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()],
    )
    power_socket_availability = SelectField(
        "Power Socket Availability",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    """ Home Page """
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    """ Add Cafe Page """
    form = CafeForm()
    
    if form.validate_on_submit():
        with open(CAFE_DATA_FILE_DIR, mode="a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},"
                           f"{form.cafe_location.data},"
                           f"{form.opening_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_strength_rating.data},"
                           f"{form.power_socket_availability.data}")
        return redirect(url_for('cafes'))
    
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    """Show all cafes in the database"""
    with open(CAFE_DATA_FILE_DIR, newline="", encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
