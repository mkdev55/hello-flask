from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'
