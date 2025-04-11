from flask import Flask, send_file, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/track/<email_id>")
def track_email(email_id):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Opened by: {email_id} - IP: {request.remote_addr}\n")

    return send_file("pixel.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
