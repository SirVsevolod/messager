#!/usr/bin/python

import requests

username = input("Enter username:")
password = input("Enter password:")

while True:
	text = input("Enter massage:")

	r = requests.post("http://127.0.0.1:5000/send",
					json = {"username":username,"password":password,"text":text}
				)
	if not r.json()["ok"]:
		print("Access denied")
		break



