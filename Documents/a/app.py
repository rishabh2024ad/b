from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Set up Flask app
app = Flask(__name__)

# Set your Gemini API key
API_KEY = ""  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def chat_with_ai(prompt):
    response = model.generate_content(prompt)
    return response.text  # Extract AI response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    ai_response = chat_with_ai(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

