from flask import Flask, jsonify, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/logo/<path:filename>")
def serve_logo(filename):
    return send_from_directory(os.path.join(BASE_DIR, "logo"), filename)

@app.route("/sound/<path:filename>")
def serve_sound(filename):
    return send_from_directory(
        os.path.join(BASE_DIR, "sound"),
        filename,
        mimetype="audio/mpeg",)

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(os.path.join(BASE_DIR, "images"), filename)

@app.route("/images-list")
def list_images():
    """Return list of promo images for rotating background."""
    image_dir = os.path.join(BASE_DIR, "images")
    allowed_exts = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

    if not os.path.isdir(image_dir):
        return jsonify([])

    files = [
        f"images/{f}"
        for f in os.listdir(image_dir)
        if os.path.splitext(f)[1].lower() in allowed_exts
    ]
    return jsonify(files)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)