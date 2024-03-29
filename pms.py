from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///./db/personal.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SQLALCHEMY_ECHO"]=True
db=SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
