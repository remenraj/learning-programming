# Blog capstone project v2
# Blog posts are stored at https://www.npoint.io/

from flask import Flask, render_template, request
from post import Post
import requests, smtplib, os


# npoint saved post url
BLOG_POSTS_NPOINT_URL = "https://api.npoint.io/a6d05d7440464327fba9"

ADMIN_EMAIL = os.getenv("EMAIL")
ADMIN_EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# getting the blog posts from npoint
posts = requests.get(BLOG_POSTS_NPOINT_URL)
posts.raise_for_status()
all_posts = posts.json()

# creating a list of post objects
post_objects = []
# create a list of Post objects
for post in all_posts:
    post_object = Post(post['id'], post['title'], post['subtitle'], post['body'], post['author'], post['date'])
    post_objects.append(post_object)

# create a Flask app
app = Flask(__name__)
    
    
@app.route('/')
def home():
    """Render the home page where all blog posts are displayed."""
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Render the post page where a single blog post is displayed."""
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """ Render the contact page where the user can submit a contact form."""
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message) -> None:
    """Send an email containing form data when the user submits the contact form."""
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(ADMIN_EMAIL, ADMIN_EMAIL_PASSWORD)
        connection.sendmail(from_addr=ADMIN_EMAIL, to_addrs=ADMIN_EMAIL, msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
