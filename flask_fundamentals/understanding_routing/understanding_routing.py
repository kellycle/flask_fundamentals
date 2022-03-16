from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi ' + name.capitalize() + '!'

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    print(num)
    print(word)
    return word * int(num)

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True)