from flask_app import app
from flask import redirect, render_template,request
from ..models.dojo import Dojo
from ..models.ninja import Ninja



@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html',all_ninjas=Ninja.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        # "age": request.form['age']
    }
    ninja_id = Ninja.save(data)
    return redirect('/ninjas')

@app.route('/ninja/<int:id>')
def show_ninja(id):
    data = {
        "id":id
    }
    return render_template('show_ninja.html',ninja=Ninja.get_by_id(data))

@app.route('/join/dojo',methods=['POST'])
def join_dojo():
    data = {
        'dojo_id': request.form['dojo_id'],
        'ninja_id': request.form['ninja_id']
    }
    return redirect(f"/ninja/{request.form['ninja_id']}")