from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "UrsoBank Online"

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/extrato")
def extrato():
    return render_template("extrato.html")

@app.route("/transferir")
def transferir():
    return render_template("transferir.html")

@app.route("/pix")
def pix():
    return render_template("pix.html")

@app.route("/saque")
def saque():
    return render_template("saque.html")

@app.route("/login")
def
