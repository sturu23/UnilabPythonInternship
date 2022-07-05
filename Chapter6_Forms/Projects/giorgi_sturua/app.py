from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from forms import LoginForm, RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():


    return render_template('base.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        gmail = form.email.data
        print(username,password,gmail)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username,password)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

