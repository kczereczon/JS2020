import sys
from datetime import datetime

dateString = sys.argv[1]
dateTime = datetime.strptime(dateString, '%Y-%m-%d')
currentDate = datetime.now()

diff = dateTime - currentDate

print(diff.days)
