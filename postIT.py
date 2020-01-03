from flask import Flask, render_template, url_for, flash, redirect

# importing the form classes from the form.py file since it's in the same directory
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

# Creating a secrete key to avoid cross platform attacks, modifying cookies,and other foreign attacks
app.config["SECRET_KEY"] = "5b358dae34397f5e261e35f22d753c7a"
# creating dummy data, which contains an array called 'posts' that holds  dictionary with key and value
Jan_posts = [
    # Creating the 1st dictionary
    {
        "author": "Osama A",
        "title": "Happy New Years",
        "content": "Hope you have a wonderful new year and inshallah your dreams can come true :)",
        "date_posted": "Jan 1, 2019",
    },
    # Creating the 2nd dictionary
    {
        "author": "Nexa D.",
        "title": "Cats",
        "content": "I love playing with my cat",
        "date_posted": "Jan 2, 2019",
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", Jan_posts=Jan_posts)


@app.route("/about")
def about():
    return render_template("about.html", titleName="About")


# Creating the registeration route
@app.route("/register", methods=["GET", "POST"])
def register():
    # Now we must create an instance of our form,hence we use '()'
    registerationForm = RegisterationForm()
    # checking if the form has the correct required input fields, in other words if it passes our required validations
    # In this case we must use a 'flash messages', thats a easy way sends the user a 1 time alert, you must import

    if registerationForm.validate_on_submit():
        # sucess is just the bootstrap CLASS that we want the alert style to be !
        # we will implement the functionality of the 'flash' method/pop up message in the layout.html 
        flash(f"Account created for {registerationForm.username.data}!", "sucess")
        # sending the user back to the home page if they successfully register
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", regForm=registerationForm)


# Creating the login form route
@app.route("/login")
def login():
    loginForm = LoginForm()
    return render_template("login.html", title="Login", signInForm=loginForm)


if __name__ == "__main__":
    app.run(debug=True)

