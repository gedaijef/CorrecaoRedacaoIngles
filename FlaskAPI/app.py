from flask import Flask, render_template

app = Flask(__name__)


#URL simples
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/salaG/<int:numero>")
def salaG(numero):
    return "Incremento é " + str(numero + 1)

#JSON
from flask import jsonify
@app.route("/json")
def json():
    return jsonify({"nome": "Germinare Tech", "sala": "salaG"})

@app.route("/json/numeros")
def json_numeros():
    return jsonify(list(range(10)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=5001)