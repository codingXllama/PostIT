from flask_wtf import FlaskForm
# importing the required fields from the wtforms
from wtforms import StringField,PasswordField,SubmitField
# importing the required validators from the wtforms.validators
from wtforms.validators import DataRequired, Length,Email,EqualTo

# creating a regeisteration form


class regeisterationForm(FlaskForm):
    # the userName passed in into the StringField method is a 'label' that will be used with in the html form
    # creating the length of userName restriction as the DataRequired
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    
    email= StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])

