from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome to SCA Cloud School Application'