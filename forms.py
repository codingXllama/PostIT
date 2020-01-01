from flask_wtf import FlaskForm

# importing the required fields from the wtforms
from wtforms import StringField, PasswordField, SubmitField, BooleanField

# importing the required validators from the wtforms.validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

# creating a regeisteration form
# Creating the required fields for registering
class RegisterationForm(FlaskForm):

    # the userName passed in into the StringField method is a 'label' that will be used with in the html form
    # creating the length of userName restriction as the DataRequired
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    # Creating the submit button field
    submit = SubmitField("Sign Up")


# Creating the LoginForm
class LoginForm(FlaskForm):
    # allowing the user to login with their email rather than userName
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    # allowing the user to stay logged in after the brower closes after some time, using a secure cookie
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")

