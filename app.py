from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("perfil.html")

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
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333)

@app.route("/")
def home():
    return "UrsoBank Online"
