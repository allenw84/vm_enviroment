#!/usr/bin/env python
from flask import Flask
from datetime import datetime
import re
import requests
from video import Video

from flask import render_template , Response
app = Flask(__name__)

buffer_frame = [] 
@app.route("/")
def home():
    return render_template('index.html')
def gen(video):
    while True:
        frame = video.get_frame()
        yield (b'--frame\r\n'  
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


@app.route("/video_feed")
def video_feed():
    """Video streaming route. """
    return Response(gen(Video),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    #content = "Hello there, " + clean_name + "! It's " + formatted_now
    return render_template(
        "hello_there.html",
        name = name,
        date = datetime.now()        
        )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__== '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,  
        debug = True,
        threaded=True
    )