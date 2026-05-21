from flask import Flask, render_template
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
