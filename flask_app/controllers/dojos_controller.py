from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja

@app.route('/')
def index():
    return redirect("/dojos")

@app.route( "/dojos", methods=["GET"] )
def get_dojos():
    list_of_dojos = Dojo.get_all()
    return render_template( "index.html", list_of_dojos = list_of_dojos )

@app.route( "/dojo/new", methods=["POST"] )
def create_dojo():
    print( request.form )
    new_dojo = {
        "name_of_dojo" : request.form["name_of_dojo"],
    }
    dojo_id = Dojo.create_one( new_dojo )
    return redirect( "/" )

