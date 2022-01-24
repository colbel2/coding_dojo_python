from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<int:x>/<int:y>')
def xy(x,y):
    #lost on how to implement the 2nd checkerboard..
    
    pass


if __name__=="__main__":
    app.run(debug=True)