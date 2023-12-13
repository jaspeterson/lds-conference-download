import os
import sys
import time

from conference import download_conference

STARTING_CONF_YEAR = 1971
START_TIME = time.time()

dir = os.getcwd()
if len(sys.argv) > 1:
    dir += "/" + sys.argv[1]
else:
    dir += "/download"
    if not os.path.exists(dir):
        os.mkdir(dir)

print("Starting Download...\n")

currTime = time.gmtime(START_TIME)
year = currTime[0]
month = currTime[1]

bothConf = True
if month >= 10:
    bothConf = True
elif month >= 4:
    bothConf = False
else:
    bothConf = True
    year -= 1

currYear = STARTING_CONF_YEAR
while currYear <= year:
    download_conference(str(currYear), "04", dir)
    if not currYear == year or bothConf:
        download_conference(str(currYear), "10", dir)
    currYear += 1

print("Finished Download")