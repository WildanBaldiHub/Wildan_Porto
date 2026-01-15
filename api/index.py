from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Ganti link ini dengan link RAW database.json milik Abang
DB_URL = "https://raw.githubusercontent.com/WildanBaldiHub/Wildan_Porto/main/api/database.json"

def get_db():
    try:
        return requests.get(DB_URL).json()
    except:
        return {"config": {"engine_active": True}, "projects": []}

@app.route('/api/predict', methods=['POST'])
def predict():
    db = get_db()
    if not db['config']['engine_active']:
        return jsonify({"reply": db['config']['maintenance_msg'], "status": "OFFLINE"})
    
    data = request.json
    return jsonify({
        "reply": f"Respon WILDAN Engine untuk: {data.get('message')}",
        "announcement": db['config']['announcement']
    })

@app.route('/api/projects', methods=['GET'])
def projects():
    return jsonify(get_db().get("projects", []))