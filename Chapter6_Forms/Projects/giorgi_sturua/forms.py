from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField()

class RegisterForm(FlaskForm):

    username = StringField(label='Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField(label='Email', validators=[DataRequired(), Email(message='Invalid email'), Length(min=5, max=50)])
    submit = SubmitField()