
import sys

old_value = ''
last_line = ''

for line in sys.stdin:
    timestamp, value = line.split(',')
    if value != old_value:
        sys.stdout.write(line)
        old_value = value
        last_line = ''
    else:
        last_line = line

sys.stdout.write(last_line)