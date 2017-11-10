from urllib.request import urlopen
import json
from tfl_url import tfl_url
	
def get_status():
	# This function will get the status for all the lines
	webpage = urlopen(tfl_url).read() # tfl_url is where my API keys are stored
	js = json.loads(webpage)
	all_lines_status = {}

	for i in range(0, len(js)):
		status_code = js[i]["lineStatuses"][0]["statusSeverity"]
		line_name = js[i]["name"]
		all_lines_status[line_name] = status_code
	return all_lines_status

def get_status_line(line):
	# This function will get the status for a given line
	webpage = urlopen(tfl_url).read()
	js = json.loads(webpage)
	all_lines_status = {}

	for i in range(0, len(js)):		
		status_code = js[i]["lineStatuses"][0]["statusSeverity"]
		line_name = js[i]["name"]
		all_lines_status[line_name] = status_code
	return all_lines_status[line]