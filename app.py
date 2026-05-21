from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

usuarios = {}

saldo = {
    "admin": 100
}


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/registrar", methods=["POST"])
def registrar():

    user = request.form["user"]
    password = request.form["password"]

    usuarios[user] = password

    return redirect("/")


@app.route("/login", methods=["POST"])
def login():

    user = request.form["user"]
    password = request.form["password"]

    if user in usuarios:

        if usuarios[user] == password:

            return redirect("/dashboard")

    return "Login inválido"


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/pix")
def pix():
    return render_template("pix.html")


@app.route("/saque", methods=["GET", "POST"])
def saque():

    usuario = "admin"

    if request.method == "POST":

        valor = float(request.form["valor"])

        if saldo[usuario] >= valor:

            saldo[usuario] -= valor

            return f"""
            <body style='background:#050b1a;color:white;font-family:Arial;padding:30px'>

            <h1>✅ Saque realizado</h1>

            <h2>Valor: R$ {valor}</h2>

            <h3>Saldo restante: R$ {saldo[usuario]}</h3>

            <a href='/dashboard' style='color:#60a5fa'>
            Voltar
            </a>

            </body>
            """

        else:

            return """
            <body style='background:#050b1a;color:white;font-family:Arial;padding:30px'>

            <h1>❌ Saldo insuficiente</h1>

            <h3>Você não possui saldo para sacar.</h3>

            <a href='/saque' style='color:#60a5fa'>
            Voltar
            </a>

            </body>
            """

    return render_template("saque.html")


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

    port = int(os.environ.get("PORT", 3333))

    import os

app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8080))
)
