
import csv

def raw_read_from_file(filename):

    """ A generator which returns tupels timestamp, value, from a file with
    given filename. """

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for record in reader:
            if len(record) == 2:
                yield record

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