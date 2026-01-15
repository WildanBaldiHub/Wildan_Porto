from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn # Sesuaikan jika arsitektur model abang pakai ini

app = Flask(__name__)
CORS(app) # Penting agar HTML bisa akses server ini

# --- LOAD MODEL WILDAN ENGINE ---
# Pastikan Class arsitektur model Abang sudah didefinisikan di sini
# Contoh: class WildanModel(nn.Module): ...
# model = WildanModel()
# model.load_state_dict(torch.load('WILDAN Engine V1.0.pth'))
# model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        user_input = data.get("message")
        
        # --- LOGIKA PROSES MODEL DISINI ---
        # Contoh simulasi output dari WILDAN Engine
        # prediction = model(convert_to_tensor(user_input))
        
        response_text = f"WILDAN Engine V1.0 Analysis: Input received. Weighted neuron path activated for '{user_input}'."
        
        return jsonify({"reply": response_text})
    except Exception as e:
        return jsonify({"reply": f"Engine Error: {str(e)}"}), 500

if __name__ == '__main__':
    print("WILDAN ENGINE V1.0 (Weighted Integrated Learning Dynamic Artificial Neuron) is Starting...")
    app.run(port=5000)