from flask_wtf import FlaskForm
from main.models import User
import email_validator
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import ValidationError,Email,DataRequired,Length, Length, EqualTo



class RegistrationForm(FlaskForm):
    username = StringField( validators=[DataRequired()])
    email = StringField( validators=[DataRequired(), Email()])
    password = PasswordField( validators=[DataRequired(),Length(min=8)])
    password2 = PasswordField(
        validators=[DataRequired(), EqualTo('password',message='The passwords must match')])
    submit = SubmitField()
