import groups
from db import db
from flask import session
import users
import plants


def get_groups():
    sql = "SELECT * FROM groups"
    result = db.session.execute(sql)
    return result.fetchall()


def add_new_group(name):
    sql = "INSERT INTO groups (name) VALUES (:name)"
    db.session.execute(sql, {"name": name})
    db.session.commit()
    return True


def remove_group(group_id):
    sql1 = "DELETE FROM group_values WHERE group_id=:group_id"
    db.session.execute(sql1, {"group_id": group_id})
    db.session.commit()
    sql2 = "DELETE FROM groups WHERE id=:group_id"
    db.session.execute(sql2, {"group_id": group_id})
    db.session.commit()
    return True


def add_to_groups(group_id, plant_id):
    sql = "INSERT INTO group_values (group_id, plant_id) " \
          "SELECT :group_id, :plant_id " \
          "WHERE NOT EXISTS " \
          "(SELECT group_id, plant_id FROM group_values WHERE group_id=:group_id AND plant_id=:plant_id)"
    db.session.execute(sql, {"group_id": group_id, "plant_id": plant_id, "id": plant_id})
    db.session.commit()
    return True


def get_group_values(group_id):
    sql = "SELECT plant_name FROM plants " \
          "INNER JOIN group_values ON plants.id=group_values.plant_id WHERE group_values.group_id=:group_id"
    result = db.session.execute(sql, {"group_id": group_id})
    return result.fetchall()

    # sql = "SELECT plant_id FROM group_values WHERE group_id=:group_id"
    # result = db.session.execute(sql, {"group_id": group_id})
    # return result.fetchall()