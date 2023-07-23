from flask import Flask
from models import db , User 

#Instanciar nuestra aplicacion de Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app) #conetca con base de datops cuand oapp se ejecuta



@app.route("/")
def home():
    return "hello flask"

@app.route("/todos", methods = ["GET"])
def get():
    return "METHOD GET"


@app.route("/todos", methods = ["POST"])
def post():
    return "METHOD POST"


@app.route("/todos", methods = ["DELETE"])
def delete():
    return "METHOD DELETE"

with app.app_context():
    db.create_all()




if __name__ == "__main__":
    app.run(host='localhost', port = 5000)
