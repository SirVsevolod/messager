#!/usr/bin/python
import requests
from time import sleep
from datetime import *

last_massage_time = 0

while True:
	r = requests.get("http://127.0.0.1:5000/history",
		params = {'after':last_massage_time})
	
	data = r.json()
	for  massage in data['messages']:

		beauty_time = datetime.fromtimestamp(massage['time'])
		beauty_time = beauty_time.strftime("%H:%M:%S")

		print(beauty_time,massage['username'])
		print(massage['text'])
		print()
		last_massage_time = massage["time"]
		
	sleep(1)