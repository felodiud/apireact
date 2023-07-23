from flask import Flask


#Instanciar nuestra aplicacion de Flask
app = Flask(__name__)


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






if __name__ == "__main__":
    app.run(host='localhost', port = 5000)
