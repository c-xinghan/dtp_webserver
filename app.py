import re
import json
from datetime import datetime, timedelta

from flask import Flask, request
from flask import render_template

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask_socketio import SocketIO, emit


app = Flask(__name__)
speed = 0.0
time = datetime.now()
socketio = SocketIO(app)

#defines the job
# def job():
#     new_price = "mum";
    #job emits on websocket
    # socketio.emit('price update', new_price, broadcast=True)

#schedule job
# scheduler = BackgroundScheduler()
# running_job = scheduler.add_job(job, 'interval', seconds=4, max_instances=1)
# scheduler.start()

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
    socketio.emit('price update', speed, broadcast=True)
    return render_template("home.html", speed=speed, time=time)

@app.route("/time/")
def get_time():
    return json.dumps(time.strftime("%H%M"))

@app.route("/decreasetime/", methods=['POST'])
def decrease_time():
    global time
    time -= timedelta(hours=1)
    return render_template("home.html", speed=speed, time=time)


@app.route("/increasetime/", methods=['POST'])
def increase_time():
    global time
    time += timedelta(hours=1)
    return render_template("home.html", speed=speed, time=time)

@app.route("/decreasespeed/", methods=['POST'])
def decrease_speed():
    global speed
    speed -= 3
    return render_template("home.html", speed=speed, time=time)


@app.route("/increasespeed/", methods=['POST'])
def increase_speed():
    global speed
    speed += 3
    return render_template("home.html", speed=speed, time=time)


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')