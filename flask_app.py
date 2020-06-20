from flask import Flask, render_template
app = Flask(__name__)


posts =  [
    {
        'author': 'Andrew Osborne',
        'title': 'First Blog',
        'content': 'First post content',
        'date_posted': 'June 20, 2020'
    },
    {
        'author': 'Seun Utulu',
        'title': 'Second Blog',
        'content': 'Seond post content',
        'date_posted': 'June 21, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home_page():
    """
    Here we are allowing ourselves to use the post variable
    in our template file and saying that the posts there would be
    equal to the posts in this file.
    """
    return render_template("home.html", posts=posts)


@app.route("/about")
def about_page():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)
