from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def fill_survey():
    return render_template('dojo.html')

@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comment = request.form['comment']
    # print request.form

    return render_template('results.html', name=name, dojo=dojo, language=language, comment=comment)

app.run(debug=True)