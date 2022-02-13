from main import app
from flask import render_template, request,flash,redirect,url_for
from main.form import RegistrationForm


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',title= "newhomepage")

@app.route("/login",methods=['GET','POST'])
def login():
    form = RegistrationForm()
    # if form.validate_on_submit:
    #     return redirect(url_for('index'))
    return render_template('signin.html', title="Login", form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    # if form.validate_on_submit:
    #     return redirect(url_for('index'))
    return render_template('register.html', title='register', form=form)


if __name__ == "__main__":
    app.run()