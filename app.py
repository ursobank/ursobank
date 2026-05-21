from flask import Flask, render_template, request, redirect

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


# EXTRATO

@app.route("/extrato")
def extrato():
    return "<h1>Extrato</h1>"


# PERFIL

@app.route("/perfil")
def perfil():
    return "<h1>Perfil UrsoBank</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
host="0.0.0.0",
port=3333
)
