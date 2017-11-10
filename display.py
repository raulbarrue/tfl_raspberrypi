from status import get_status # Importing the functions defined in the other script
import time
import os

while True: # Infinite loop to constantly show the data (refreshed every 30 seconds)
	all_lines = get_status() # Get the status of all lines
	for lines in all_lines:
		if all_lines[lines] == 10:
			print(lines + ": Good Service")
		elif all_lines[lines] == 6:
			print(lines + ": Severe Delays")
		elif all_lines[lines] == 9:
			print(lines + ": Minor Delays")
	time.sleep(30) # Data will refresh every 30 seconds
	os.system("cls") # This will clean the command screen

