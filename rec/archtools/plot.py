
import sys
import os
from datetime import datetime
import config

print('set grid')
print('set xdata time')
print('set timefmt "%Y-%m-%dT%H:%M:%S"')
print('set format x "%H:%M"')
sys.stdout.write('plot ')

vars = list([v for a in sys.argv for v in config.ARCH_VARIABLES if a == v['arch-id']])

# print plot arguments
for v in vars:
    title = v['plot-title'] if 'plot-title' in v else v['arch-id']
    color = 'linecolor "{}"'.format(v['plot-color']) if 'plot-color' in v else ''
    sys.stdout.write('"-" using 1:2 with lines {} title "{}" , '.format(color, title))
sys.stdout.write(';\n')

# print out the data
for v in vars:
    file_name = ''.join((config.ARCH_DIR, v['arch-file']))
    with open(file_name, 'r') as f:
        for line in f:
            timestamp, value = line.split(',')
            sys.stdout.write('{} {}'.format(timestamp, value))
    print('e\n')