from status import get_status_line # Importing the functions defined in the other script
import time
import os
from blinkt import set_pixel, show, set_brightness

while True:
    
    lines = ["Circle", "District", "Victoria", "Central", "Piccadilly", "Metropolitan", "Jubilee", "Bakerloo"]
    lines_status = []    
    for line in lines:
        status1 = get_status_line(line)
        lines_status.append(status1)
    
    pixel = 0
    for status2 in lines_status:
        if status2 == 10:
            set_brightness(0.1)
            set_pixel(pixel, 0, 255, 0)
            show()
            print(lines[pixel] + ": Good Service")
        else:
            set_brightness(0.5)
            set_pixel(pixel, 255, 0, 0)
            show()
            print(lines[pixel] + ": Bad Service")
        pixel += 1

    time.sleep(30) # Data will refresh every 30 seconds
    os.system("cls") # This will clean the command screen