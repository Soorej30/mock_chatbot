from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI key here
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful career assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.7
        )
        bot_reply = response["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
