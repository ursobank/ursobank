from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>UrsoBank Online</h1>
    <p>Servidor funcionando.</p>

    <a href='/perfil'>Perfil</a><br>
    <a href='/extrato'>Extrato</a><br>
    <a href='/transferir'>Transferir</a>
    """


@app.route("/extrato")
def extrato():
    return render_template("extrato.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route("/transferir")
def transferir():
    return render_template("transferir.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333)
