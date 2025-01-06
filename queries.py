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

def get_user_by_username(username):
    sql_get_user = f"""
    SELECT id, password
    FROM users
    WHERE username = '{username}'"""
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