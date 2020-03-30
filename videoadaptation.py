from flask import Flask
#import request
import os
import time 
from configparser import ConfigParser
from datetime import datetime

app = Flask(__name__)
@app.route('/')

def get_videoadaptation():
	res='"service":"AdaptationStrategyCreator"'
	while True:
		start = time.time()
		parser = ConfigParser()
		parser.read('dev.ini')
		parser.read('speed.ini')
		#parser.read('average.ini')

		rate1 = parser.get('rate', 'rate1')
		rate2 = parser.get('rate', 'rate2')
		scale1 = parser.get('rate', 'scale1')
		scale2 = parser.get('rate', 'scale2')

		average = int(parser.get('rate', 'average'))


		sn = float(parser.get('bandwidth', 'speed'))
		if ( sn > average ):
			framerate = rate1
			scale = scale1
			twoframerate = (int(framerate) * 2)
		else:
			framerate = rate2
			scale = scale2
			twoframerate = (int(framerate) * 2)

		print("Threshold=", average)
		print("Internet speed=", sn)
		print("Framerate=", framerate)

		f = open("frame.txt", "w")
		f.write("framerate="+framerate+"\n")
		f.write("scale="+scale+"\n")
		f.write("twoframerate="+str(twoframerate))
		f.close

		now = datetime.now()
		print("Time=", now)

		end = time.time()
		print("execution time=", end - start)
		print("----------")
		time.sleep(2)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5002)
