from status import get_status # Importing the functions defined in the other script
import time
import os

while True: # Infinite loop to constantly show the data (refreshed every 30 seconds)
	all_lines = get_status() # Get the status of all lines
	for line in all_lines:
		if all_lines[line] == 10:
			print(line + ": Good Service")
		elif all_lines[line] == 6:
			print(line + ": Severe Delays")
		elif all_lines[line] == 9:
			print(line + ": Minor Delays")
		elif all_lines[line] == 5:
			print(line + ": Part Closure")
		elif all_lines[line] == 20:
			print(line + ": Service Closed")
		elif all_lines[line] == 3:
			print(line + ": Part Suspended")
		else:
			print(line + ": Unknown Status")
	time.sleep(30) # Data will refresh every 30 seconds
	os.system("cls") # This will clean the command screen

