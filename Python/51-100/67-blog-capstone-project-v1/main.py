# Blog capstone project v1
# Blog posts are stored at https://www.npoint.io/

from flask import Flask, render_template
from post import Post
import requests, datetime


# current year
year = datetime.datetime.now().year

# npoint saved post url
BLOG_POSTS_NPOINT_URL = "https://api.npoint.io/4af156202f984d3464c3"

# getting the blog posts from npoint
posts = requests.get(BLOG_POSTS_NPOINT_URL)
posts.raise_for_status()
all_posts = posts.json()

# creating a list of post objects
post_objects = []
# create a list of Post objects
for post in all_posts:
    post_object = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_object)

# create a Flask app
app = Flask(__name__)
    
    
@app.route('/')
def home():
    """Render the home page where all blog posts are displayed."""
    return render_template("index.html", all_posts=post_objects, year=year)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Render the post page where a single blog post is displayed."""
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
            print(requested_post.subtitle)

    return render_template("post.html", post=requested_post, year=year)


if __name__ == "__main__":
    app.run(debug=True)
