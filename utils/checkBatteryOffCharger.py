import time
from datetime import datetime
import psutil
import sys

def loopForever():
	while(True):
		battery = psutil.sensors_battery()
		percent = battery.percent
		if not battery.power_plugged:
			print("-----------------------------------------------------------")
			print('checking power percentage off charger','|', datetime.now())
			print("-----------------------------------------------------------")
			if percent<30:
				sys.stdout.write('\a')
				sys.stdout.flush()
				print("-----------------------------------------------------------")
				print('battery at 30 percent','|', datetime.now())
				print("-----------------------------------------------------------")
		else:
			print("-----------------------------------------------------------")
			print('charger plugged','|', datetime.now())
			print("-----------------------------------------------------------")
			if percent>=95:
				sys.stdout.write('\a')
				sys.stdout.flush()
				print("-----------------------------------------------------------")
				print('battery nearly full with {} percent, remove charger'.format(percent), '|', datetime.now())
				print("-----------------------------------------------------------")
		
		time.sleep(300)
		print("-----------------------------------------------------------")
		print('5 minutes lapsed', '|', datetime.now())
		print("-----------------------------------------------------------")
				
if __name__ == "__main__":
	print("-----------------------------------------------------------")
	print('battery power warning notifier running', '|', datetime.now())
	print("-----------------------------------------------------------")
	loopForever()
