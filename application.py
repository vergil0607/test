from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hallo Leni!</h1>"