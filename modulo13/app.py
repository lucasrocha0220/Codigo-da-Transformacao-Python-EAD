'''
pip install flask
pip install flask flask-jwt-extended


'''

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Bem-vindo à API Flask!"}), 200


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Envie 'nome' e 'email' no formato JSON"}), 400

    nome = dados["nome"]
    email = dados["email"]

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!",
        "usuario": {
            "id": user_id,
            "nome": nome,
            "email": email
        }
    }), 201


if __name__ == "__main__":
    app.run(debug=True)