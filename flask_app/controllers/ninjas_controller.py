from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo = Dojo.get_one_dojo({'dojo_id': dojo_id})
    return render_template('show.html', dojo=dojo)

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('create.html', dojos=dojos)


@app.route('/ninjas', methods=['POST'])
def add_ninja():
    Ninja.save(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")

