from flask import Blueprint, request, flash, redirect, url_for
from flask.templating import render_template
import flask_sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

from . import db
from .models import User

auths = Blueprint('auths', __name__)


@auths.route('/sign-up', methods=['GET', 'POST'])
def signup_view():
    form_data = request.form
    print(form_data)
    if request.method == "POST":
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists!", category="error")

        elif len(email) < 4:
            flash("Email must be atleast 4 characters. ", category="error")
        elif len(fullName) < 2:
            flash("Name must be atleast 2 characters. ", category="error")
        elif len(password1) < 7 or len(password2) < 7:
            flash("Password length must be atleast 8 characters", category="error")
        elif password1 != password2:
            flash("Passwords does not match", category="error")
        else:
            # Create a user to db
            new_user = User(email=email, full_name=fullName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created succesfully.", category="success")
            return redirect(url_for('views.home_view'))

    return render_template("sign_up.html", user=current_user)


@auths.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print("User is validated... Logging in")
                login_user(user, remember=True)
                flash("Logged in Successfully!" ,category="success")
                return redirect(url_for('views.home_view'))
            else:
                flash("Incorrect Password!", category="error")
        else:
            flash("User does not exits", category="error")

    return render_template("login.html", user=current_user)


@auths.route('/logout')
@login_required
def logout_view():
    logout_user()
    return redirect(url_for('auths.login_view'))

