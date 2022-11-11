from flask import Flask, jsonify
from team import getTeam

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_news(): 
    return jsonify(getTeam.getAll())

if __name__ == "__main__":
    app.run()