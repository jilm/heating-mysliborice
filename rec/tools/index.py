
import sys
import config
import daq
import pathlib
from datetime import datetime

def inspect_file(filename):

    """ Go through the given arch file and returns data for the index,
    it means, the name of the variable, first and last timestamp, the
    number of records and finally extreme values. """

    counter = 0
    first_timestamp = ''
    last_timestamp = ''
    # open given file
    records = daq.raw_read_from_file(filename)
    temp, var_name = records.__next__()
    for r in records:
        if len(r) == 2:
            counter += 1
            last_timestamp, value = r
            if counter == 1:
                first_timestamp = last_timestamp
    return str(filename), var_name, first_timestamp, last_timestamp, counter

def update_index():
    files = config.ARCH_PATH.glob('*.arch')
    records = [inspect_file(f) for f in files]
    for r in records:
        print(','.join(str(x) for x in r))


def load_index():
    index = []
    index_path = pathlib.Path(config.ARCH_PATH, 'index')
    with open(index_path) as index_file:
        index = index_file.read()
    index = index.split('\n')
    index = [r.split(',') for r in index]
    index = [
        {
            'file': pathlib.Path(r[0]),
            'name': r[1],
            'first_timestamp': datetime.strptime(r[2], '%Y-%m-%dT%H:%M:%S'),
            'last_timestamp': datetime.strptime(r[3], '%Y-%m-%dT%H:%M:%S'),
            'count': int(r[4])
        }
        for r in index if len(r) == 5
    ]
    return index

def filter_variable(index, variable):
    return [r for r in index if variable == r['name']]

def filter_timestamp(index, t1, t2):
    return [r for r in index if timestamp_intersection((t1, t2), (r['first_timestamp'], r['last_timestamp']))]

def timestamp_intersection(t1, t2):
    # find greater begen time
    intersection_start = t1[0] if t1[0] > t2[0] else t2[0]
    # and the smaller and time
    interscetion_end = t1[1] if t1[1] < t2[1] else t2[1]
    # and compare them
    if intersection_start < interscetion_end:
        return intersection_start, interscetion_end
    else:
        return None

if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = inspect_file(filename)
        print(','.join(str(x) for x in result))
    else:
        update_index()

