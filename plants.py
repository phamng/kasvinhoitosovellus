import plants
from db import db
from flask import session
import users


def get_list():
    sql = "SELECT P.id, P.plant_name, P.sun, P.water FROM plants P"
    result = db.session.execute(sql)
    return result.fetchall()


def get_plant_name(id):
    sql = "SELECT plant_name FROM plants WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()[0]


def get_plant_sun(id):
    sql = "SELECT sun FROM plants WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()[0]


def get_plant_water(id):
    sql = "SELECT water FROM plants WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()[0]


def send(plant_name, sun, water):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO plants (plant_name, sun, water) VALUES (:plant_name, :sun, :water)"
    db.session.execute(sql, {"plant_name": plant_name, "sun": sun, "water": water})
    db.session.commit()
    return True


def search(plant_name):
    sql = "SELECT id, plant_name, sun, water FROM plants WHERE plant_name LIKE :plant_name"
    result = db.session.execute(sql, {"plant_name": "%" + str(plant_name) + "%"})
    return result.fetchall()


def add_comment(content, plant_id):
    sql = "INSERT INTO comments (content, plant_id) VALUES (:content, :plant_id)"
    db.session.execute(sql, {"content": content, "plant_id": plant_id})
    db.session.commit()
    return True


def remove_comment(content, plant_id):
    sql = "DELETE FROM comments WHERE content=:content AND plant_id=:plant_id"
    db.session.execute(sql, {"content": content, "plant_id": plant_id})
    db.session.commit()
    return True


def get_comment(id):
    sql = "SELECT C.content FROM comments C WHERE C.plant_id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchall()

def get_comment_id(id):
    sql = "SELECT C.id FROM comments C WHERE C.plant_id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchall()

def remove_plant(id):
    sql1 = "DELETE FROM comments WHERE plant_id=:id"
    db.session.execute(sql1, {"id": id})
    db.session.commit()
    sql2 = "DELETE FROM plants WHERE id=:id"
    db.session.execute(sql2, {"id": id})
    db.session.commit()
    return True


def get_groups():
    sql = "SELECT id, name FROM groups"
    result = db.session.execute(sql)
    return result.fetchall()


def get_like_count(plant_id):
    sql = "SELECT COUNT(*) FROM likes WHERE plant_id=:plant_id"
    result = db.session.execute(sql, {"plant_id": plant_id})
    return result.fetchone()[0]


def update_likes(user_id, plant_id):
    sql = "INSERT INTO likes (user_id, plant_id) " \
          "SELECT :user_id, :plant_id " \
          "WHERE NOT EXISTS (SELECT user_id, plant_id FROM likes WHERE user_id=:user_id AND plant_id=:plant_id)"
    db.session.execute(sql, {"user_id": user_id, "plant_id": plant_id})
    db.session.commit()
    return True