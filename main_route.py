from flask import Blueprint, request, render_template, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, secrets
import queries
from flask import render_template
from flask import session
#from werkzeug.security import check_password_hash
main_routes = Blueprint('main_routes', __name__)

@main_routes.route("/")
def index():
    return render_template("front_page.html")


@main_routes.route("/account", methods=["POST"])
def have_account():
    #if "csrf_token" not in session:
            #session["csrf_token"] = secrets.token_hex(16)
    #if session["csrf_token"] != request.form["csrf_token"]:
        #abort(403)

    have_account = request.form.get("have_account")
    if have_account == "No":
        return redirect(url_for("main_routes.new_account"))
    elif have_account == "Yes":
        return redirect(url_for("main_routes.login"))


@main_routes.route("/new_account", methods=["GET", "POST"])
def new_account():
    if request.method == 'POST':
        #if session["csrf_token"] != request.form["csrf_token"]:
            #abort(403)

        username = request.form["username"]
        password = request.form["password"]
        #hash_value = generate_password_hash(password)

        if queries.get_user_id(username):
            flash("This username is not available, please choose another username")
            return redirect(url_for("main_routes.new_account"))
        else:
            queries.new_user(username, password)
            #queries.new_user(username, hashvalue)

        return redirect(url_for("main_routes.login"))
    return render_template("create_account.html")


@main_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #if session["csrf_token"] != request.form["csrf_token"]:
            #abort(403)

        username = request.form["username"]
        password = request.form["password"]

        user = queries.get_user_by_username(username)

        if not user:
            flash("Wrong username")
            return redirect(url_for("main_routes.login"))
        #else:
            #hash_value = user.password

        if user.password == password:
            session['username'] = username
            #Here the authentication succeeds even if an attacker guesses or intercepts the plain-text passworn
            #corrected version:

            #if check_password_hash(hash_value, password):
                #session['username'] = username
        else:
            flash("Incorrect password!")
            return redirect(url_for("main_routes.login"))

    return render_template("login.html")


@main_routes.route('/logout')
def logout_student():
    del session["username"]
    return redirect(url_for('main_routes.index'))