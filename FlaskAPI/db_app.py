from flask import Flask, render_template, request
import psycopg 

app = Flask(__name__)


def get_connection():
    return psycopg.connect("")


#URL simples
@app.route("/")
def home():
    return render_template("home.html")


@app.get("/api/sala/<int:id>")
def get_sala(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sala WHERE id = %s", (id,))
    result = cursor.fetchone()[1]
    conn.close() 
    return {"id": id, "sala": result}


@app.post("/api/sala")
def add_sala():
    conn = get_connection()
    cursor = conn.cursor()

    data = request.get_json()
    titulo = data["titulo"]

    cursor.execute("INSERT INTO sala (titulo) VALUES (%s) RETURNING id",(titulo,))
    sala_id = cursor.fetchone()[0]
    #fechar
    conn.commit()
    cursor.close()
    conn.close() 
    return {"sala_id": sala_id, "message:": "Sala criada com sucesso"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=5002)