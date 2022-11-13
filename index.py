from flask import Flask, render_template, jsonify, request
from module.team import get_team
from module import match


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
    todo={}
    return jsonify(match.getAllMatch(todo))

@app.route("/match/get-by-date", methods=["GET"])
def getMatchByDate():
    rq=request.args
    date = rq.get('date')   
    print(rq)
    
    return jsonify(match.getAllMatch(rq))


if __name__ == "__main__":
    app.run()
