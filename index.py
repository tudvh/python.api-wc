from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_news(): 
    return jsonify({"data": "tus"})

if __name__ == "__main__":
    app.run()