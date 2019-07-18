from flask import Flask, render_template, url_for, request, send_file, Response
import requests
import time
from flask_socketio   import SocketIO, emit
from random import random
from time import sleep
from threading import Thread, Event

import json


#App Flask Declaration
app = Flask(__name__, static_url_path="", static_folder="static", template_folder='templates')
#Asyc socket.io
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = Thread()

@app.route("/")
@app.route("/console")
def home():
    return render_template('console.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        #Start the main bot thread, where all the sub-processes are childs of
        thread = Console()
        thread.start()



@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


def message(string):
    socketio.emit('newnumber', {'number': string}, namespace='/test')


def messagePandL(value):
    socketio.emit('pandl', {'number': value}, namespace='/test')
def messageOpen(value):
    socketio.emit('open_positions', {'number': value}, namespace='/test')



class Console(Thread):
    def __init__(self):
        self.delay = 1
        super(Console, self).__init__()

    def start(self):      
        sleep(self.delay)
        message("Calculating Scores... ")



    def run(self):
        self.start()
if __name__ == '__main__':
    socketio.run(app)


