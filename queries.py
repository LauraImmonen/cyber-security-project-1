from db import db
from sqlalchemy.sql import text

def new_user(username, password):
    sql_insert = f"""
    INSERT INTO users (username, password)
    VALUES ('{username}', '{password}')"""

    db.session.execute(text(sql_insert))
    db.session.commit()

#password should be stored as hash value in the database, not as plain text
#The code above is also vulnerable for injection, since it uses direct user input

#def new_user(username, hash_value):
    #sql_insert = """
    #INSERT INTO users (username, password)
    #VALUES (:username, :password)"""
    #db.session.execute(text(sql_insert), {"username": username, "password": hash_value})
    #db.session.commit()

def get_user_id(username):
    sql_get_user_id = f"""
    SELECT id FROM users
    WHERE username='{username}'"""

    result = db.session.execute(text(sql_get_user_id))
    user_id = result.fetchone()

    if user_id:
        return user_id
    return False

# This code is vulnerable to SQL Injection because it is directly inserting user input into the query

#def get_user_id(username):
    #sql_get_user_id = """
    #SELECT id FROM users
    #WHERE username=:username"""
    #result = db.session.execute(text(sql_get_user_id), {"username": username})
    #user_id = result.fetchone()

    #if user_id:
        #return user_id
    #False

def get_user_by_username(username, password):
    sql_get_user = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    result = db.session.execute(text(sql_get_user))
    return result.fetchone()

#There is a SQL injection vulnerability in the above query

#def get_user_by_username(username):
    #sql_get_user = """
    #SELECT id, password
    #FROM users
    #WHERE username = :username"""
    #result = db.session.execute(text(sql_get_user), {"username": username})
    #return result.fetchone()

def get_username():
    sql_get_user = f"""
    SELECT username FROM profiles"""

    result = db.session.execute(text(sql_get_user))
    return result.fetchall()

def get_profile_by_username(username):
    sql_get_profile = f"""
    SELECT p.username, p.nickname, p.hobbies, p.interests, p.fav_color, p.fav_food, p.fav_movie
    FROM profiles p
    WHERE p.username = '{username}'
    """
    result = db.session.execute(text(sql_get_profile))
    return result.fetchone()

#There is a SQL injection vulnerability in the above query

#def get_profile_by_username(username):
    #sql_get_profile = """
    #SELECT p.profile_id, p.username, p.nickname, p.hobbies, p.interests, p.fav_color, p.fav_food, p.fav_movie
    #FROM profiles p
    #WHERE p.username = :username"""
    #result = db.session.execute(text(sql_get_profile), {"username": username})
    #return result.fetchone()

def insert_profile(username, nickname, hobbies, interests, fav_color, fav_food, fav_movie):
    sql_get_user_id = f"""
    SELECT id FROM users WHERE username = '{username}'"""

    result = db.session.execute(text(sql_get_user_id))
    user_id = result.fetchone()

    if user_id is None:
        raise ValueError("No user with this name")
    user_id = user_id[0]

    sql_insert_profile = f"""
    INSERT INTO profiles (profile_id, username, nickname, hobbies, interests,
    fav_color, fav_food, fav_movie)VALUES
    ({user_id}, '{username}', '{nickname}', '{hobbies}',
    '{interests}', '{fav_color}', '{fav_food}', '{fav_movie}')"""

    db.session.execute(text(sql_insert_profile))
    db.session.commit()

#def insert_profile(username, hobbies, interests, fav_color, fav_food, fav_movie):
    # We use parameterized query to avoid SQL injection in this version
    #sql_get_user_id = """
    #SELECT id FROM users WHERE username = :username"""
    #result = db.session.execute(text(sql_get_user_id), {'username': username})
    #user_id = result.fetchone()
    #if user_id is None:
        #raise ValueError("No user with this name")
    #user_id = user_id[0]
    #sql_insert_profile = """
    #INSERT INTO profiles (profile_id, username, hobbies, interests, fav_color, fav_food, fav_movie)
    #VALUES (:user_id, :username, :nickname,:hobbies, :interests, :fav_color, :fav_food, :fav_movie)"""
    #db.session.execute(text(sql_insert_profile), {
        #'user_id': user_id, 'username': username, 'nickname': nickname, 'hobbies': hobbies,
        #'interests': interests, 'fav_color': fav_color, 'fav_food': fav_food, 'fav_movie': fav_movie})
    #db.session.commit()

def existing_profile(username):
    sql_count_profile = """SELECT COUNT(*) FROM profiles WHERE username = :username"""

    result = db.session.execute(text(sql_count_profile), {'username': username})
    count = result.scalar()

    return count > 0
