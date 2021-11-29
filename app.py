from flask import Flask, render_template, request, jsonify

from chatterbot import ChatBot
from chatbot_corpus import my_bot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")


@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    print(text)
    # todo: check if text is valid
    response = f"{my_bot.get_response(text)}"
    message={"answer":response}
    return jsonify(message)
    
if __name__ == "__main__":
    app.run(debug=True)
