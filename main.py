from flask import Flask, request, jsonify, send_from_directory
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

app = Flask(__name__, static_folder="static")

# Khởi tạo client
client = genai.Client(api_key=api_key)

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "Xin chào!")
        
        # Gọi model Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",  # hoặc model bạn có quyền dùng
            contents=prompt
        )
        
        return jsonify({"ok": True, "text": response.text})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
