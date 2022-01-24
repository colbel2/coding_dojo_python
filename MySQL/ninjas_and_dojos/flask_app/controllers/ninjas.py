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
        "title":request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    ninja_id = Ninja.save(data)
    return redirect('/ninjas')

@app.route('/ninja/<int:id>')
def show_ninja(id):
    data = {
        "id":id
    }
    return render_template('show_ninja.html',ninja=Ninja.get_by_id(data),unfavorited_dojos=Dojo.unfavorited_dojos(data))

@app.route('/join/dojo',methods=['POST'])
def join_dojo():
    data = {
        'dojo_id': request.form['dojo_id'],
        'ninja_id': request.form['ninja_id']
    }
    Dojo.add_favorite(data)
    return redirect(f"/ninja/{request.form['ninja_id']}")