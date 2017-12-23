
import re
import sys
from datetime import datetime

ARCH_VARIABLES = [
    {
        'arch-id': 'outdoor-temp',
        'arch-file': 'outtemp',
        'archive': True
    }, {
        'arch-id': 'heater-temp',
        'arch-file': 'heattemp',
        'archive': True
    }
]

# Read header from the stdin
head = list([h.strip() for h in sys.stdin.readline().split(',')])

# Open file for writing for each variable
files = list([None for h in head])
for i, h in enumerate(head):
    for v in ARCH_VARIABLES:
        if v['archive'] and v['arch-id'] == h:
            files[i] = open(v['arch-file'], 'w')

# Split all of the values from stdin into the opened files
for line in sys.stdin:
    splitted = line.split(',')
    for i, f in enumerate(files):
        if f:
            f.write('{},{}\n'.format(splitted[0], splitted[i]))

# Close all of the files
for f in files:
    if f:
        f.close()