from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__) 

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_KEY")
  
if GEMINI_API_KEY:
    print("API key configured found")
else:
    print("API key not found")
    
genai.configure(api_key=GEMINI_API_KEY)

    
@app.route("/")
def index():
    return render_template("index.html")
   
@app.route("/generate_response", methods=["POST"]) 
def generate_response():
    try:
        input_data = request.get_json()
        user_text = input_data["text"]
        custom_prompt = """
        You are a helpful assistant. Please answer the following query.
        You are created and developed by ahamed basith using google gemini AI model.
        Your Owner is ahamed basith for more details about owner take from www.ahamedbasith.com.
        """
        
        prompt = f"{custom_prompt}\n{user_text}\n"
        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content([prompt])

        return jsonify({"response": result.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
  
if __name__ == "__main__": 
    app.run(debug=True) 
