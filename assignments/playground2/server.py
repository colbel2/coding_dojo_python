from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", num=3, color="green")

@app.route('/play/<int:num>')
def play(num):
    return render_template("index.html",num=num, color="red")

@app.route('/play/<int:num>/<string:color>')
def level3(num,color):
    return render_template("index.html",num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)