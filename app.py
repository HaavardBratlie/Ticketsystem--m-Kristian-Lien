from flask import Flask, render_template, request, redirect, session, jsonify, url_for
import mysql.connector
import random

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
            ticket_id VARCHAR(8) NOT NULL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            henvendelse TEXT NOT NULL,
            message TEXT NOT NULL,
            status ENUM('ikke påbegynt', 'under behandling', 'oppklart') DEFAULT 'ikke påbegynt'
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
def henvendelser():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    cursor.close()  
    conn.close()
    return render_template("henvendelser.html", tickets=tickets)

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        henvendelse = request.form['henvendelse']
        message = request.form['message']

        ticket_id = f"#{random.randint(1000000, 9999999)}"

        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tickets (ticket_id, name, email, henvendelse, message)
                VALUES (%s, %s, %s, %s, %s)
            ''', (ticket_id, name, email, henvendelse, message))
            conn.commit()
            
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return redirect(url_for("bekreft"))

    return render_template('send.html')

@app.route("/status")
def status():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT henvendelse, name, status, ticket_id FROM tickets")
    tickets = cursor.fetchall()
    cursor.close()  
    conn.close()
    return render_template("status.html", tickets=tickets)
    
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

@app.route("/detaljer/<ticket_id>")
def detaljer(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets WHERE ticket_id = %s", (ticket_id,))
    ticket = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("detaljer.html", ticket=ticket)

@app.route("/oppdater_status/<ticket_id>", methods=["POST"])
def oppdater_status(ticket_id):
    new_status = request.form.get("status")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET status = %s WHERE ticket_id = %s", (new_status, ticket_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("henvendelser"))
     
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")