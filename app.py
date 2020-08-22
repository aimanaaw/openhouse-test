from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! Testing out the flask app"


@app.route('/<name>')
def user(name):
	return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()