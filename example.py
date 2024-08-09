from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

class UserModel:
    pass

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
