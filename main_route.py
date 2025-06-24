from flask import Blueprint, request, render_template, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, secrets
import queries
from flask import render_template
from flask import session
import bleach
from werkzeug.security import check_password_hash

main_routes = Blueprint('main_routes', __name__)

@main_routes.route("/", methods=["GET"])
def index():
    #if "csrf_token" not in session:
            #session["csrf_token"] = secrets.token_hex(16)
    return render_template("front_page.html")

@main_routes.route("/account", methods=["POST"])
def have_account():
    #if session["csrf_token"] != request.form.get("csrf_token"):
        #abort(403)

    have_account = request.form.get("have_account")
    if have_account == "No":
        return redirect(url_for("main_routes.new_account"))
    elif have_account == "Yes":
        return redirect(url_for("main_routes.login"))


@main_routes.route("/new_account", methods=["GET", "POST"])
def new_account():
    if request.method == 'POST':
        #if session["csrf_token"] != request.form.get("csrf_token"):
            #abort(403)

        username = request.form["username"]
        password = request.form["password"]
        #hash_value = generate_password_hash(password)

        if queries.get_user_id(username):
            flash("This username is not available, please choose another username")
            return redirect(url_for("main_routes.new_account"))
        else:
            queries.new_user(username, password)
            #queries.new_user(username, hash_value)

        return redirect(url_for("main_routes.login"))
    return render_template("create_account.html")


@main_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #if session["csrf_token"] != request.form.get("csrf_token"):
            #abort(403)

        username = request.form["username"]
        password = request.form["password"]

        #The above has xss vulnerability, we need to use flask bleach to
        #prevent users from injecting scripts

        #username = bleach.clean(request.form["username"])
        #password = bleach.clean(request.form["password"])

        user = queries.get_user_by_username(username)

        if not user:
            flash("Wrong username")
            return redirect(url_for("main_routes.login"))
        #else:
            #hash_value = user.password

        if user.password == password:
            session['username'] = username
            return redirect(url_for("main_routes.profiles_list"))

        #corrected version:
        #if check_password_hash(hash_value, password):
            #session['username'] = username
        else:
            flash("Incorrect password!")
            return redirect(url_for("main_routes.login"))

    return render_template("login.html")


@main_routes.route("/profiles_list")
def profiles_list():
    #We check if user is logged in and what their username is
    #username = session.get("username")
    #if not username:
    #If no one is logged in, we redirect to login page
        #flash("You must be logged in to view profiles.")
        #return redirect(url_for("main_routes.login"))

    profiles = queries.get_username()

    #user_has_profile = queries.existing_profile(username=username)

    if not profiles:
        flash("There are no profiles yet")


    return render_template("profiles_list_page.html", profiles = profiles)#, user_has_profile=user_has_profile)


@main_routes.route("/view_profile/<username>")
def view_profile(username):
    #username = session.get("username")
    #if not username:
    #return redirect(url_for("main_routes.login"))

    profile = queries.get_profile_by_username(username)

    if profile:
        username = profile[0]
        nickname = profile[1]
        hobbies = profile[2]
        interests = profile[3]
        fav_color = profile[4]
        fav_food = profile[5]
        fav_movie = profile[6]

        return render_template("view_profile.html", username=username,
                               nickname=nickname, hobbies=hobbies, interests=interests,
                               fav_color=fav_color, fav_food=fav_food, fav_movie=fav_movie)
    else:
        flash("Profile not found!")
        return redirect(url_for("main_routes.profiles_list"))


@main_routes.route("/create_your_profile", methods = ["POST", "GET"])
def create_your_profile():
    if request.method == "GET":
        return render_template("create_profile.html")

    #username = session.get("username")
    #if not username:
        #flash("You must be logged in to create a profile!")
        #return redirect(url_for("main_routes.login"))

    username = request.form["username"]
    nickname = request.form["nickname"]
    hobbies = request.form["hobbies"]
    interests = request.form["interests"]
    fav_color = request.form["fav_color"]
    fav_food = request.form["fav_food"]
    fav_movie = request.form["fav_movie"]

    #The above has xss vulnerability, we need to use flask bleach to
    #prevent users from injecting scripts

    #nickname = bleach.clean(request.form["nickname"])
    #hobbies = bleach.clean(request.form["hobbies"])
    #interests = bleach.clean(request.form["interests"])
    #fav_color = bleach.clean(request.form["fav_color"])
    #fav_food = bleach.clean(request.form["fav_food"])
    #fav_movie = bleach.clean(request.form["fav_movie"])

    if queries.existing_profile(username):
        flash("This user already has a profile!")
        return redirect(url_for("main_routes.profiles_list", username=username))

    if not all([username, nickname, hobbies, interests, fav_color, fav_food, fav_movie]):
            flash("Please fill out all the required fields!")
            return redirect(url_for("main_routes.create_your_profile"))

    queries.insert_profile(username, nickname, hobbies, interests, fav_color, fav_food, fav_movie)

    flash("Profile created successfully!")
    return redirect(url_for("main_routes.profiles_list"))


@main_routes.route('/logout')
def logout_student():
    del session["username"]
    return redirect(url_for('main_routes.index'))