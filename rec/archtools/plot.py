
import sys
from datetime import datetime

print('set xdata time')
print('set timefmt "%y-%m-%dT%H:%M:%S"')
print('set xrange ["2017-12-09T20:40:41":"2017-12-17T12:44:00"]')
print('plot "-" using 1:2 with lines;')


for line in sys.stdin:
    timestamp, value = line.split(',')
    sys.stdout.write('{:.0f} {}'.format(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S').timestamp(), value))

print('e')