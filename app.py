import json
from datetime import datetime, timedelta

from flask import Flask, request, redirect, render_template, session, url_for

# from urllib.parse import urlencode
# from urllib.request import Request, urlopen

from flask_socketio import SocketIO


app = Flask(__name__)
speed = 0.0
time = datetime.now()
socketio = SocketIO(app)
# development key, replace with your own
app.secret_key = 'dti'

@app.route("/")
def home():
    return render_template("home.html", speed=speed, time=time)

@app.route("/speed/")
def get_speed():
    return json.dumps(speed)

@app.route("/updatespeed/", methods=['POST'])
def update_speed():
    global speed     
    speed = float(request.headers.get('speed'))
    socketio.emit('speed update', speed, broadcast=True)
    return redirect(url_for("home"))

@app.route("/time/")
def get_time():
    return json.dumps(time.strftime("%H%M"))

@app.route("/decreasetime/", methods=['POST'])
def decrease_time():
    global time
    time -= timedelta(hours=1)
    return redirect(url_for("home"))

@app.route("/increasetime/", methods=['POST'])
def increase_time():
    global time
    time += timedelta(hours=1)
    session['speed'], session['time'] = speed, time
    return redirect(url_for("home"))

@app.route("/decreasespeed/", methods=['POST'])
def decrease_speed():
    global speed
    speed -= 3
    return redirect(url_for("home"))

@app.route("/increasespeed/", methods=['POST'])
def increase_speed():
    global speed
    speed += 3
    return redirect(url_for("home"))
    # return render_template("home.html", speed=speed, time=time)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')