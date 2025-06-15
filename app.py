from flask import Flask, request, render_template
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("location.html")

@app.route("/submit_location", methods=["POST"])
def submit_location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    print(f"Friend's location: {lat}, {lon}")  # Printed only in your terminal
    return "OK", 200

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
