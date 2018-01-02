
import sys
import os
from datetime import datetime
import config
import daq

def print_plot(variable, data):

    print('set grid')
    print('set xdata time')
    print('set timefmt "%Y-%m-%dT%H:%M:%S"')
    print('set format x "%H:%M"')
    sys.stdout.write('plot "-" using 1:2 with lines;\n')
    for time, value in data:
        sys.stdout.write('{} {}\n'.format(time.isoformat(), value))
    sys.stdout.write('e\n')


    #vars = list([v for a in sys.argv for v in config.ARCH_VARIABLES if a == v['arch-id']])

    # print plot arguments
    #for v in vars:
    #    title = v['plot-title'] if 'plot-title' in v else v['arch-id']
    #    color = 'linecolor "{}"'.format(v['plot-color']) if 'plot-color' in v else ''
    #    sys.stdout.write('"-" using 1:2 with lines {} title "{}" , '.format(color, title))
    #sys.stdout.write(';\n')

    # print out the data
    #for v in vars:
    #    file_name = ''.join((config.ARCH_DIR, v['arch-file']))
    #    with open(file_name, 'r') as f:
    #        for line in f:
    #            timestamp, value = line.split(',')
    #            sys.stdout.write('{} {}'.format(timestamp, value))
    #    print('e\n')

if __name__ == "__main__":
    variable = sys.argv[1]
    time_interval = (
        datetime.strptime(sys.argv[2], '%Y-%m-%dT%H:%M:%S'),
        datetime.strptime(sys.argv[3], '%Y-%m-%dT%H:%M:%S')
    )
    print_plot(variable, daq.get(variable, time_interval))
