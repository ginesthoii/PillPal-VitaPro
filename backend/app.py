from flask import Flask, request, jsonify
from api_clients import get_supplement_interactions, get_supplement_recommendations
import os

app = Flask(__name__)

# Load API keys from environment variables
OPENFDA_KEY = os.getenv("OPENFDA_KEY")
RXNORM_KEY = os.getenv("RXNORM_KEY")
NIH_SUPP_KEY = os.getenv("NIH_SUPP_KEY")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    if not data or "supplements" not in data:
        return jsonify({"error": "Missing supplements list"}), 400
    suggestions = get_supplement_recommendations(data["supplements"])
    return jsonify({"suggestions": suggestions})

@app.route("/interactions", methods=["POST"])
def interactions():
    data = request.get_json()
    if not data or "prescriptions" not in data or "supplements" not in data:
        return jsonify({"error": "Missing prescriptions or supplements"}), 400
    interactions = get_supplement_interactions(
        prescriptions=data["prescriptions"],
        supplements=data["supplements"]
    )
    return jsonify({"interactions": interactions})

if __name__ == "__main__":
    app.run(debug=True)
