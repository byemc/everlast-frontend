import datetime

from flask import Flask, jsonify, render_template, url_for

# from mcstatus import JavaServer

app = Flask(__name__)


DATA = {
    "version": "Pre-launch",
    "nextversion": "release 1.0.0",
    "startTime": 1669852799000,  # unix millies
    "endTime": 1671128400000,  # unix millies
}


@app.route("/")
def index():
    return render_template("index.html", DATA=DATA)


@app.template_filter()
def toShortTime(value):
    value = datetime.datetime.fromtimestamp(value / 1000)
    return value.strftime("%e %b %Y %H:%M %z")


# Won't work until 1.7

# @app.route("/ping")
# def ping():
#     server = JavaServer.lookup("everlast.byemc.live")
#     status = server.status()
#     print(status)
#     return str(status.players.online)


app.run(debug=True)
