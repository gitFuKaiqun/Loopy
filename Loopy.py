__author__ = 'Kaiqun'

from Monitor import newfiledetector
from xlsParsor import onefileoperate
import datetime
import time

if __name__ == '__main__':
	while True:
		TheQueue = newfiledetector('testingData', datetime.datetime.now().strftime('%Y'))
		if TheQueue == []:
			print 'here'
		else:
			for onefile in TheQueue:
				onefileoperate(onefile)
		time.sleep(30)