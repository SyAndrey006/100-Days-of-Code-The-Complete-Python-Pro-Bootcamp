from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

hello_world()

#set FLASK_APP=hello.py
#python -m flask run