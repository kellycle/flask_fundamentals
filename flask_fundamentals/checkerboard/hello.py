from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", width=8, height=8)

@app.route('/<int:x>')
def checker_x(x):
    return render_template("index.html", width=int(x), height=8)

@app.route('/<int:x>/<int:y>')
def checker_x_y(x, y):
    return render_template("index.html", width=int(x), height=int(y))

# @app.route('/<int:x>/<int:y>/<color1>/<color2>')
# def checker_x_y_color(x, y, color1, color2):
#     return render_template("index.html", width=int(x), height=int(y), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)