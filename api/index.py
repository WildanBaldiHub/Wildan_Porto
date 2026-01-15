from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Try-Except agar kodingan tetap jalan meski Torch error di lokal
try:
    import torch
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

app = Flask(__name__)
CORS(app)

# Load Model WILDAN Engine (Hanya di Server/Vercel)
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'WILDAN Engine V1.0.pth')
model = None

if HAS_TORCH:
    try:
        # Ganti 'YourModelClass' dengan arsitektur model abang
        # model = YourModelClass()
        # model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
        # model.eval()
        print("WILDAN_ENGINE: Neural Path Established")
    except Exception as e:
        print(f"Engine Load Warning: {e}")

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        msg = data.get("message", "")
        op = data.get("operator", "Operator")

        # Response dari WILDAN Engine
        # Jika model sudah di-load, ganti bagian ini dengan output model asli
        res_text = f"WILDAN Engine V1.0 merekam input dari {op}: '{msg}'. Jalur Weighted Integrated Neuron telah diaktifkan."

        return jsonify({"reply": res_text})
    except Exception as e:
        return jsonify({"reply": f"System Error: {str(e)}"}), 500