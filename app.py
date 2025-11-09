from flask import Flask, jsonify, request
import json

app = Flask(__name__)

ALLOWED_ORIGIN = "https://atalanteav.rf.gd/"  # sadece bu site erişebilir
SECRET_KEY = "atalantebaba123"           # opsiyonel: token koruma

@app.route("/api/data")
def get_data():
    # CORS kontrolü
    origin = request.headers.get("Origin")
    if origin != ALLOWED_ORIGIN:
        return jsonify({"error": "Yetkisiz erişim"}), 403

    # Token kontrolü (opsiyonel)
    token = request.args.get("key")
    if token != SECRET_KEY:
        return jsonify({"error": "Geçersiz token"}), 403

    # JSON dosyasını oku ve gönder
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
