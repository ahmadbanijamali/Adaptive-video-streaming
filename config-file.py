import time

from configparser import ConfigParser
config = ConfigParser()

#while True:

config['rate'] = {
	'rate1': '60',
	'rate2': '30',
	'scale1': '720:480',
	'scale2': '320:240',
	'average': 'xx'
}

with open('./dev.ini', 'w') as f:
	config.write(f)
	#time.sleep(10)
