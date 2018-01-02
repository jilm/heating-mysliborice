
import sys
import csv
import index
from datetime import datetime

def raw_read_from_file(filename):

    """ A generator which returns tupels timestamp, value, from a file with
    given filename. """

    head = True
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for record in reader:
            if head:
                head = False
                continue
            if len(record) == 2:
                yield record

def raw_read_from_files(filenames):
    for f in filenames:
        for r in raw_read_from_file(f):
            yield r

def cast_timestamp(raw_data):
    for timestamp, value in raw_data:
        timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
        yield timestamp, value

def filter_timestamp(data, time_interval):
    for time, value in data:
        if time >= time_interval[0] and time <= time_interval[1]:
            yield time, value

def get(variable, timestamp):
    # find appropriate records in index
    idx = index.load_index()
    idx = index.filter_variable(idx, variable)
    idx = list(index.filter_timestamp(idx, timestamp[0], timestamp[1]))
    # sort them
    if idx:
        #idx = idx.sort(key=lambda x: x['first_timestamp'])
        data = filter_timestamp(
            cast_timestamp(
                raw_read_from_files(r['file'] for r in idx)
            )
            , timestamp
        )
        for r in data:
            yield r

def reduce_dup(records):

    """ A generator which removes consecutive duplicit values from the input
    iterable. It expects and returns an interable of tupels: timestamp,
    value. """

    value = ''
    timestamp = ''
    old_value = ''
    last = False
    for timestamp, value in records:
        last = value != old_value
        if last:
            yield timestamp, value
            old_value = value
    if not last:
        yield timestamp, value


if __name__ == "__main__":
    variable = sys.argv[1]
    time_interval = (
        datetime.strptime(sys.argv[2], '%Y-%m-%dT%H:%M:%S'),
        datetime.strptime(sys.argv[3], '%Y-%m-%dT%H:%M:%S')
    )
    for time, value in get(variable, time_interval):
        print('{},{}'.format(time.isoformat(), value))
