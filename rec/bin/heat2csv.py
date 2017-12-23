
import re
import sys
from datetime import datetime

first_line = True

MONTH_NAMES = {'Dec': 12}

def convert_timestamp(timestamp):
    wday, month, day, hour, minute, sec, tz, year = re.split('\s|:', timestamp)
    dt = datetime(
        int(year),
        MONTH_NAMES[month],
        int(day),
        int(hour),
        int(minute),
        int(sec)
    )
    return dt.isoformat()

for line in sys.stdin:
    match = re.findall('DataResponse\{(.*)\}', line)
    if match:
        signals = match[0].split(',')
        splitted = list([re.split('=|;', sig) for sig in signals])
        if first_line:
            head = ','.join([sig[0] for sig in splitted])
            print('timestamp,{}'.format(head))
            first_line = False
        values = ','.join([sig[3] for sig in splitted])
        timestamp = convert_timestamp(splitted[0][1])
        print('{},{}'.format(timestamp,values))

