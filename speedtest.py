from flask import Flask
import requests
import os
import re
import subprocess
from datetime import datetime
import time

app = Flask(__name__)
@app.route('/')
def get_speed():
	res='{"Service":"SpeedTest"}\n'
	while True:
		start = time.time()
		response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

#ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
#download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
		upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

#ping[0] = ping[0].replace(',', '.')
#download[0] = download[0].replace(',', '.')
		upload[0] = upload[0].replace(',', '.')

#try:
#    if os.stat('/home/pi/speedtest/speedtest.csv').st_size == 0:
#        print 'Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)'
#except:
#    pass

#print ping[0], download[0], upload[0]
		internetspeed = float(upload[0])
#exit(speed)
		print("Internet speed=", internetspeed)
		from configparser import ConfigParser

		config = ConfigParser()

		config['bandwidth'] = {
			'speed': internetspeed
		}

		with open('./speed.ini', 'w') as f:
			config.write(f)

		now = datetime.now()

		end = time.time()
		print("Time=", now)
		print("Execution time=", end - start)
		print("----------")


	#time.sleep(10)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5001)
