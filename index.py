from flask import Flask, render_template
from module.team import get_team

app = Flask(__name__)


@app.route("/team/get-all", methods=["GET"])
def getTeam():
    return get_team.get_all()

@app.route("/team/get-by-group/<id_group>", methods=["GET"])
def getTeamByGroup(id_group):
    return get_team.get_by_group(id_group)

@app.route("/", methods=["GET"])
def getDocument():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run()
