from flask import Flask, send_file, request
import datetime
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/track/<email_id>")
def track_email(email_id):
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Build log dictionary
    log_data = {
        "timestamp": str(datetime.datetime.now()),
        "email_id": email_id,
        "ip_address": ip_address,
        "method": request.method,
        "path": request.path,
        "full_url": request.url,
        "base_url": request.base_url,
        "host": request.host,
        "referrer": request.referrer,
        "user_agent": request.headers.get("User-Agent"),
        "content_type": request.content_type,
        "content_length": request.content_length,
        "query_params": request.args.to_dict(),
        "form_data": request.form.to_dict(),
        "json_data": request.get_json(silent=True),
        "cookies": request.cookies.to_dict(),
        "headers": dict(request.headers),
        "remote_addr": request.remote_addr,
        "environ_keys": {k: str(v) for k, v in request.environ.items()},
        "request": request
    }
    # Log to file
    with open("detailed_log.json", "a") as f:
        f.write(json.dumps(log_data, indent=2) + ",\n")
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Opened by: {email_id} - IP: {request.remote_addr}\n")

    return send_file("pixel.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
