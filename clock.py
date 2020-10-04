from datetime import datetime
from time import sleep

while True:
	now = datetime.now()
	sleep(1)
	print('Current Time is:')
	print('%s:%s:%s' % (str(now.hour).zfill(2), str(now.minute).zfill(2), str(now.second).zfill(2)))
