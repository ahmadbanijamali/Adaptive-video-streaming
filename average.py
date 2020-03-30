from flask import Flask
import requests
import os
import time
from configparser import ConfigParser
from array import *

app = Flask(__name__)
@app.route('/')

def get_average():
	s = array('i', [])
	i = 0
	average = 20
	res='{"Service":"Average"}\n'
	#res=res + response.content.decode('utf-8')
	while True:
		start = time.time()
		parser = ConfigParser()
		parser.read('speed.ini')

		sn = float(parser.get('bandwidth', 'speed'))


		s.append(int(sn))
		if ( i > 9):
			average = 0
			sum = 0
			b = 0
			k = 0
			for i in range (0, 10):
				if (s[i] > 26):
					b += 1
				else:
					k +=1
			for i in range (0, 10):
				sum = sum + s[i]
			if (b >= k):
				average = (sum/100)
			else:
				average = 26
			s.pop(0)

		print(s)
		print(average)

		config = ConfigParser()
		config['averagespeed'] = {
			'average': average
		}

		with open('./average.ini', 'w') as f:
			config.write(f)

		end = time.time()
		print(end - start)
		time.sleep(10)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5000)
