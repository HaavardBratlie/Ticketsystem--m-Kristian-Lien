from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        # host="10.2.3.108",
        # user="haavard",
        # password="1234567",
        # database="ticket_system"
        host="127.0.0.1",
        user = "flaskuser",
        password = "password",
        database = "ticketsystem"
    )

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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")