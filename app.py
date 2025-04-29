from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Predefined moving packages
MOVING_PACKAGES = [
    {"id": 1, "name": "Starter Package", "items": ["Boxes", "Tape", "Labels"]},
    {"id": 2, "name": "Family Package", "items": ["Large Boxes", "Bubble Wrap", "Markers"]},
    {"id": 3, "name": "Premium Package", "items": ["Wardrobe Boxes", "Dolly", "Packing Paper"]},
    {"id": 4, "name": "Eco Package", "items": ["Reusable Totes", "Recyclable Wrap", "Cloth Covers"]},
]

@app.route('/')
def home():
    return "Welcome to the Moving Packages API. Use the /api/moving-packages endpoint to generate a package."

@app.route('/api/moving-packages', methods=['POST'])
def generate_package():
    data = request.json
    if not isinstance(data, dict) or "mover_name" not in data:
        return jsonify({"error": "Invalid input. 'mover_name' is required."}), 400
    
    mover_name = data["mover_name"]
    selected_package = random.choice(MOVING_PACKAGES)
    
    return jsonify({
        "message": f"Hello {mover_name}, we've selected a package for you!",
        "package": selected_package
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
