import datetime

from flask import Flask, jsonify, render_template, url_for

# from mcstatus import JavaServer

app = Flask(__name__)


DATA = {
    "version": "1.0",
    "nextversion": "release 1.1",
    "startTime": 1671130431000,  # unix millies
    "endTime": 1674241200000,  # unix millies
}

news = [
    {
        "date": "Dec 10 2022",
        "title": "[byemc.xyz] Everlast // Second time's the charm",
        "url": "https://byemc.xyz/blog/everlast-second-times-the-charm",
    }
]


@app.route("/")
def index():
    return render_template("index.html", DATA=DATA, news=news)


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


app.run(debug=True, port=5001)
