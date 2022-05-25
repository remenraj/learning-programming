# Flask Authentication example program

# downloading files: https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_from_directory
# Hashing Passwords using Werkzeug: https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security
# Flask Login Documentation: https://flask-login.readthedocs.io/en/latest/
# Flash messages: https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
# Passing authentication status to templates: https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)


app = Flask(__name__)

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///users.db"  # sqlite database file path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to suppress warning message
db = SQLAlchemy(app)  # initialize database


# Flask Login Configuration
login_manager = LoginManager()
login_manager.init_app(app)

# Flask Login User Model
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# user table in database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route("/")
def home():
    """Homepage"""
    # Every render_template has a logged_in variable set.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""

    if request.method == "POST":
        # creating a new user object
        new_user = User(
            email=request.form.get("email"),
            name=request.form.get("name"),
            password=generate_password_hash(
                password=request.form.get("password"),
                method="pbkdf2:sha256",
                salt_length=8,
            ),  # hashed and salted password
        )

        # adding the data to the database
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        # redirecting to the secrets page after registering the user
        return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email entered.
        user = User.query.filter_by(email=email).first()

        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")   # flash message
            return redirect(url_for('login'))
        
        # Password incorrect
        elif not check_password_hash(user.password, password):  # Check stored password hash against entered password hashed.
            flash('Password incorrect, please try again.')  # flash message
            return redirect(url_for('login'))
        
        # Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    # print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/logout")
def logout():
    """Logout the current user"""
    logout_user()
    return redirect(url_for('home'))


@app.route("/download")
def download():
    """Download the file"""
    # @app.route('/download/path:filename')
    # def download(filename):
    # return send_from_directory(
    # directory='static/files', path=filename, as_attachment=True
    # )
    try:
        return send_from_directory("static", path="files/cheat_sheet.pdf")

    except FileNotFoundError:
        print("File not found")

    # another way:
    # return send_file("static/files/cheat_sheet.pdf")
    # remember to import send_file from flask
    # documentation:
    # https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_file


if __name__ == "__main__":
    app.run(debug=True)
