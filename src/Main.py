from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

# An endpoint to interact with Telegram mini app
@app.route("/telegram", methods=["GET", "POST"])
def telegram():
    if request.method == "POST":
        # This is where you can process data sent from the Telegram mini app.
        data = request.get_json()
        app.logger.info("Received Telegram data: %s", data)
        # You can add any processing or saving logic here.
        return jsonify({"status": "success", "message": "Data received"}), 200
    else:
        # For a GET request, you might simply return a message or a mini page.
        return "<h2>Telegram Mini App Endpoint</h2>", 200

if __name__ == "__main__":
    # Running on all interfaces so Render can access it.
    app.run(host="0.0.0.0", port=5000)
