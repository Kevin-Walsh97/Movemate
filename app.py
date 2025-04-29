from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Predefined moving packages
MOVING_PACKAGES = [
    {"id": 1, "name": "Starter Package", "items": ["Boxes", "Tape", "Labels"]},
    {"id": 2, "name": "Family Package", "items": ["Large Boxes", "Bubble Wrap", "Markers"]},
    {"id": 3, "name": "Premium Package", "items": ["Wardrobe Boxes", "Dolly", "Packing Paper"]},
    {"id": 4, "name": "Eco Package", "items": ["Reusable Totes", "Recyclable Wrap", "Cloth Covers"]},
]

MOVING_COMPANIES = [
    {"name": "Walsh Movers", "rate": "$4,000"},
    {"name": "City Express Movers", "rate": "$3,500"},
    {"name": "Budget Movers", "rate": "$2,800"},
]

APPLIANCE_OPTIONS = [
    {"name": "Kitchenware from Bed Bath and Beyond", "price": "$200"},
    {"name": "Living Room Set from IKEA", "price": "$1,500"},
    {"name": "Bedroom Set from Wayfair", "price": "$1,200"},
]

FAKE_APARTMENTS = [
    {"name": "Downtown Studio", "price": "$1,200/month", "dimensions": "500 sq ft", "image": "https://via.placeholder.com/150"},
    {"name": "1-Bedroom Apartment", "price": "$1,800/month", "dimensions": "750 sq ft", "image": "https://via.placeholder.com/150"},
    {"name": "2-Bedroom Apartment", "price": "$2,500/month", "dimensions": "1,000 sq ft", "image": "https://via.placeholder.com/150"},
    {"name": "3-Bedroom Apartment", "price": "$3,200/month", "dimensions": "1,500 sq ft", "image": "https://via.placeholder.com/150"},
]

@app.route('/api/moving-packages', methods=['POST'])
def generate_package():
    data = request.json
    if not data or not all(key in data for key in ['name', 'current_city', 'future_city', 'bringing_bed', 'bringing_appliances', 'apartment_size']):
        return jsonify({"error": "Invalid input. All fields are required."}), 400
    
    user_details = {
        "name": data["name"],
        "current_city": data["current_city"],
        "future_city": data["future_city"],
        "bringing_bed": data["bringing_bed"],
        "bringing_appliances": data["bringing_appliances"],
        "apartment_size": data["apartment_size"],
    }

    selected_package = random.choice(MOVING_PACKAGES)
    selected_company = random.choice(MOVING_COMPANIES)
    selected_appliance = random.choice(APPLIANCE_OPTIONS)
    selected_apartment = random.choice(FAKE_APARTMENTS)

    return jsonify({
        "message": f"Hello {user_details['name']}, here's your personalized moving package!",
        "moving_package": selected_package,
        "moving_company": selected_company,
        "appliance_option": selected_appliance,
        "apartment": selected_apartment
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
