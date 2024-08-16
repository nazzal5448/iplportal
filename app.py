from flask import Flask, jsonify, request
import ipl

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"

@app.route("/api/teams")
def get_teams():
    dict={
        "teams":ipl.teams
    }
    return jsonify(dict)

@app.route("/api/teamvteam")
def teamvteam():
    team1=request.args.get("team1")
    team2=request.args.get("team2")
    response=ipl.teamVteam(team1, team2)
    return jsonify(response)

@app.route("/api/teamrecord")
def teamApi():
    team=request.args.get("team")
    response=ipl.teamRecord(team)
    return jsonify(response)
app.run(debug=True)