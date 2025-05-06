from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_db_connection():
    return mysql.connector.connect(
        host="10.2.3.127",
        user="flaskuser",
        password="password",
        database="ticket_system"
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            brukernavn VARCHAR(50),
            passord VARCHAR(50)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            hendvendelse TEXT NOT NULL,
            message TEXT NOT NULL,
            status ENUM('ikke påbegynt', 'under behandling', 'oppklart') DEFAULT 'ikke påbegynt',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_db()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/henvendelser")
def hendbendelser():
    return render_template("henvendelser.html")

@app.route("/send")
def send():
    return render_template("send.html")

@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/bekreft")
def bekreft():
    return render_template("bekreft.html")

@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tickets")
        rows = cursor.fetchall()
        cursor.close()

        tickets = []

        for row in rows:
            tickets.append(row)

        return jsonify({'status': 'success', 'message': 'Retrieved tickets', 'tickets': tickets}), 200
    
    except Exception as e:
         return jsonify({'status': 'error', 'message': 'Failed to retrieve tickets', 'error': str(e)}), 500


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = request.form["brukernavn"]
        password = request.form["passord"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin_users WHERE brukernavn = %s AND passord = %s", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["admin_logged_in"] = True
            session["admin_username"] = username
            return redirect("/")
        else:
            return render_template("admin.html", error="Feil brukernavn eller passord!")
    
    return render_template("admin.html")

@app.route("/logout")
def logout():
    session.clear()    
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")