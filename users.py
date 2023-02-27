from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash, secrets


def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False


def logout():
    del session["user_id"]


def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)


def user_id():
    return session.get("user_id", 0)


def contains_whitespace(str):
    if " " in str:
        return False

def username_used(username):
    sql = "SELECT username FROM users WHERE username=:username RETURNING id"
    result = db.session.execute(sql, {"username": username})

    if id is None:
        return True
