from app import app
from flask import render_template, request, redirect
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
    if plants.send(plant_name, sun, water):
        return redirect("/user_page")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("welcome.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        userType = request.form["user_type"]
        if userType == "user" and users.login(username, password):
            return redirect("/user_page")
        elif userType == "administrator" and users.login(username, password):
            return redirect("/admin_page")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")


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
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        elif users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/plant/<int:id>")
def result(id):
    plant_name = plants.get_plantName(id)
    sun = plants.get_plantSun(id)
    water = plants.get_plantWater(id)
    comments = plants.getComment(id)
    return render_template("plant.html", id=id, plant_name=plant_name, sun=sun, water=water, comments=comments)


@app.route("/add", methods=["POST"])
def add():
    content = request.form["content"]
    plant_id = request.form["plant_id"]
    if plants.addComment(content, plant_id):
        return redirect("/plant/" + str(plant_id))
    else:
        return render_template("error.html", message="Kommentin lähetys ei onnistunut")


@app.route("/remove", methods=["GET", "POST"])
def remove():
    plant_id = request.form["plant_id"]
    if plants.removePlant(plant_id):
        return redirect("/admin_page")
    else:
        return render_template("error.html", message="Kasvin poistaminen ei onnistunut")
