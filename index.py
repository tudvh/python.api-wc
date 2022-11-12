from flask import Flask, jsonify
from Module.team import getTeam
from Module import Match


app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_news(): 
    return getTeam.getAll()
@app.route("/get", methods=["GET"])
def getAll():
    return jsonify( Match.getAllMatch())
if __name__ == "__main__":
    app.run()