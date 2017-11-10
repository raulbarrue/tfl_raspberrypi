from status import get_status
import time
import os

while True:
	all_lines = get_status()
	for lines in all_lines:
		if all_lines[lines] == 10:
			print(lines + ": Good Service")
		elif all_lines[lines] == 6:
			print(lines + ": Severe Delays")
		elif all_lines[lines] == 9:
			print(lines + ": Minor Delays")
	time.sleep(30)
	os.system("cls")

