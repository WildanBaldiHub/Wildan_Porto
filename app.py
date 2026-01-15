from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn
import os

app = Flask(__name__)
CORS(app)

# --- DEFINISI MODEL ---
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.layer = nn.Linear(10, 2) # Sesuaikan dengan model Abang

    def forward(self, x):
        return self.layer(x)

# --- LOAD MODEL ---
model = MyModel()
if os.path.exists('model_anda.pth'):
    model.load_state_dict(torch.load('model_anda.pth', map_location=torch.device('cpu')))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('message')
    # Tambahkan logika prediksi Abang di sini
    return jsonify({"reply": f"AI Permanen (Render) menjawab: {data}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
