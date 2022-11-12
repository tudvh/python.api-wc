from flask import Flask, render_template, jsonify
from module1.team import get_team
from module1 import match


app = Flask(__name__)


@app.route("/", methods=["GET"])
def getWelcome():
    return render_template('welcome.html')


@app.route("/team/get-all", methods=["GET"])
def getTeam():
    return get_team.get_all()


@app.route("/team/get-by-group/<id_group>", methods=["GET"])
def getTeamByGroup(id_group):
    return get_team.get_by_group(id_group)


@app.route("/match/get-all", methods=["GET"])
def getAll():
    return jsonify(match.getAllMatch())


if __name__ == "__main__":
    app.run()
