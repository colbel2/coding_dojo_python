from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask import flash
from flask_app.models.show import Show

@app.route('/dashboard')
def exam_dashboard():
    if 'user_id' not in session:
        flash("This page is only available once logged in!")
        return redirect('/')

    shows = Show.get_all_shows()


    return render_template('shows.html', shows = shows)

@app.route('/show/new')
def new_show():
    return render_template('new_show.html')

@app.route('/show/create', methods=['POST'])
def create_show():
    if Show.validate_show(request.form):
        data = {
            'title': request.form['show_title'],
            'network': request.form['show_network'],
            'release_date': request.form['show_release_date'],
            'description': request.form['show_description'],
            'user_id': session['user_id']
        }
        Show.create_new_show(data)
        return redirect(f'/dashboard')
    else:

        return redirect('/show/new')

@app.route('/show/<int:show_id>')
def info_show_data(show_id):
    data = {
        'id': show_id
    }

    show = Show.get_show_by_id(data)

    return render_template('info_show.html', show = show)

@app.route('/show/<int:show_id>/delete')
def delete_show(show_id):
    data = {
        'id' : show_id
    }
    show = Show.get_show_by_id(data)
    show = Show.delete_show(data)

    if show.user_id == session['user_id']:
        Show.delete_show('/dashboard')

    return redirect ('/dashboard')


@app.route('/show/<int:show_id>/edit')
def edit_show(show_id):
    data = {
        'id': show_id
    }

    show = Show.get_show_by_id(data)
    if show.user_id != session['user_id']:
        return redirect('/dashboard')
    return render_template('edit.html', show = show)

@app.route('/show/<int:show_id>/update', methods = ['POST'])
def update_show(show_id):
    data = {
        'id': show_id
    }

    show = Show.get_show_by_id(data)
    if show.user_id != session['user_id']:
        return redirect('/dashboard')
    if Show.validate_show(request.form):
        data = {
            'title': request.form['show_title'],
            'network': request.form['show_network'],
            'release_date': request.form['show_release_date'],
            'description': request.form['show_description'],
            'id' : show_id
        }
        Show.update_show(data)
        return redirect(f'/show/{show_id}')
    else:
        return redirect(f'/show/{show_id}/edit')