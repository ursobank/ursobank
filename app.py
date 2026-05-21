from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

usuarios = {}

saldo = {
    "admin": 100
}


# LOGIN

@app.route("/")
def home():
    return render_template("login.html")


# CADASTRO

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/registrar", methods=["POST"])
def registrar():

    user = request.form["user"]
    password = request.form["password"]

    usuarios[user] = password

    return redirect("/")


# LOGIN REAL

@app.route("/login", methods=["POST"])
def login():

    user = request.form["user"]
    password = request.form["password"]

    if user in usuarios:

        if usuarios[user] == password:

            return redirect("/dashboard")

    return "Login inválido"


# DASHBOARD

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# PIX

@app.route("/pix")
def pix():
    return render_template("pix.html")


# SAQUE

@app.route("/saque", methods=["GET", "POST"])
def saque():

    usuario = "admin"
