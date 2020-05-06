#!/usr/bin/python
import time
from datetime import datetime
from flask import Flask,request


app = Flask(__name__)

messages = [{"username":"jack","text":"Hello",'time':time.time()}]

users = {"jack":"black"}

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    return {
    	"status": True,
    	"time":datetime.now().strftime("%H:%M:%S")
    }


@app.route("/send",methods = ["POST"])
def send():
	"""
	request{"username":"str","text":"str"}
	response{"ok":true}
	"""
	data = request.json
	username = data['username']
	password = data['password']
	text = data['text']
	
	if username in users:
		real_password = users[username]
		if real_password != password:
			return{"ok":False}
	else:
		users[username] = password

	messages.append({"username":username,"text":text,'time':time.time()})

	return{"ok": True}

@app.route("/history")
def history():
	after = float(request.args['after'])

	filter_messages = []

	for message in messages:
		if after < message["time"]:
			filter_messages.append(message)


	return{'messages':filter_messages}

app.run()