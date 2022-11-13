from flask import Flask, render_template, jsonify, request
from module.team import get_team
from module import match
import json
from module import xu_li


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
    data = {
        'status': 'success',
        'data': match.getAllMatch()
    }
    return data


@app.route("/match/get-by-status", methods=["GET"])
def getMatchByDate():
    rq = request.args

    if ('status' not in rq):
        data = {
            'status': 'success',
            'data': match.getMatch(None)
        }
    else:
        if (xu_li.isNum(rq['status']) or xu_li.isBool(rq['status']) == False):
            data = {
                'status': 'error',
                'data': 'status is bool'
            }
        else:
            todo = eval(rq['status'].title())

            data = {
                'status': 'success',
                'data': match.getMatch(todo)
            }

    return data


if __name__ == "__main__":
    app.run()
