import plants
from db import db
from flask import session
import users


def get_list():
    sql = "SELECT P.id, P.plant_name, P.sun, P.water FROM plants P"
    result = db.session.execute(sql)
    return result.fetchall()


def get_plantName(id):
    sql = "SELECT plant_name FROM plants WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()[0]


def get_plantSun(id):
    sql = "SELECT sun FROM plants WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()[0]


def get_plantWater(id):
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

def addComment(content, plant_id):
    sql = "INSERT INTO comments (content, plant_id) VALUES (:content, :plant_id)"
    db.session.execute(sql, {"content": content, "plant_id": plant_id})
    db.session.commit()
    return True


def getComment(id):
    sql = "SELECT C.content FROM comments C WHERE C.plant_id=:id"
    result = db.session.execute(sql, {"id": id})
    return result.fetchall()
