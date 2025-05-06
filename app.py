from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tickets")
def tickets():
    return render_template("henvendelser.html")

@app.route("/send")
def send():
    return render_template("send.html")

@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/confirm")
def confirm():
    return render_template("bekreft.html")


