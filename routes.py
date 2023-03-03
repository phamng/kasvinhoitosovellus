from app import app
from flask import render_template, request, redirect, session
import plants, users


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/user_page")
def index():
    myList = plants.get_list()
    return render_template("index.html", count=len(myList), plants=myList)


@app.route("/admin_page")
def index2():
    myList = plants.get_list()
    return render_template("index2.html", count=len(myList), plants=myList)


@app.route("/new_plant")
def new():
    return render_template("new_plant.html")


@app.route("/send", methods=["POST"])
def send():
    plant_name = request.form["plant_name"]
    sun = request.form["sun"]
    water = request.form["water"]
    if users.session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if plants.send(plant_name, sun, water):
        return redirect("/user_page")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/search", methods=["GET", "POST"])
def search():
    name = request.form["search"]
    if users.session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    fetched_plants = plants.search(name)
    return render_template("index.html", count=len(fetched_plants), plants=fetched_plants)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("welcome.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_type = request.form["user_type"]
        ##TODO: if user_type is not selected -> Do something
        if user_type == "user" and users.login(username, password):
            return redirect("/user_page")
        elif user_type == "administrator" and users.login(username, password):
            return redirect("/admin_page")
        else:
            return render_template("welcome.html", error="Väärä tunnus tai salasana!")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        # if users.user_id() == 0:
        #     return render_template("register.html", error="Käyttäjätunnus ei saatavilla!")
        if users.contains_whitespace(username) is False or users.contains_whitespace(password1) is False:
            return render_template("register.html", error="Käyttäjän nimi tai salasana ei ole kelvollinen!")
        if len(username) < 3 or len(password1) < 3:
            return render_template("register.html", error="Vähintään 3 merkkiä täytyy käyttää!")
        if password1 != password2:
            return render_template("register.html", error="Salasanat eivät täsmää!")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("register.html", error="Rekisteröinti ei onnistunut!")


@app.route("/plant/<int:id>")
def user_plant_details(id):
    plant_name = plants.get_plant_name(id)
    sun = plants.get_plant_sun(id)
    water = plants.get_plant_water(id)
    comments = plants.get_comment(id)
    like_count = plants.get_like_count(id)
    return render_template("plant.html", id=id, plant_name=plant_name, sun=sun, water=water, comments=comments, count=like_count)


@app.route("/plant2/<int:id>")
def admin_plant_details(id):
    plant_name = plants.get_plant_name(id)
    sun = plants.get_plant_sun(id)
    water = plants.get_plant_water(id)
    comments = plants.get_comment(id)
    like_count = plants.get_like_count(id)
    return render_template("plant2.html", id=id, plant_name=plant_name, sun=sun, water=water, comments=comments, count=like_count)


@app.route("/add", methods=["POST"])
def add():
    content = request.form["content"]
    plant_id = request.form["plant_id"]
    if users.session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if content != "":
        plants.add_comment(content, plant_id)
        return redirect("/plant/" + str(plant_id))
    if content == "":
        return redirect("/plant/" + str(plant_id))
    else:
        return render_template("error.html", message="Kommentin lähetys ei onnistunut")


@app.route("/remove_plant", methods=["GET", "POST"])
def remove_plant():
    plant_id = request.form["plant_id"]
    if users.session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if plants.remove_plant(plant_id):
        return redirect("/admin_page")
    else:
        return render_template("error.html", message="Kasvin poistaminen ei onnistunut")


@app.route("/remove_comment", methods=["GET", "POST"])
def remove_comment():
    content = request.form["content"]
    plant_id = request.form["plant_id"]
    if users.session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if plants.remove_comment(content, plant_id):
        return redirect("/plant2/" + str(plant_id))
    else:
        return render_template("error.html", message="Kommentin poistaminen ei onnistunut")

@app.route("/group")
def group():
   # myList = plants.get_groups()
    return render_template("groups.html")


@app.route("/like", methods=["GET", "POST"])
def like():
    plant_id = request.form["plant_id"]
    user_id = users.user_id()
    if users.session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if plants.update_likes(user_id, plant_id):
        return redirect("/plant/" + str(plant_id))
    else:
        return render_template("error.html", message="Tykkääminen ei onnistunut")