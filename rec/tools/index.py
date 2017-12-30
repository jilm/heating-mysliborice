import sys
import config
import daq

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
    return var_name, first_timestamp, last_timestamp, counter

def update_index():
    files = config.ARCH_PATH.glob('*.arch')
    records = [inspect_file(f) for f in files]
    for r in records:
        print(','.join(str(x) for x in r))



if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = inspect_file(filename)
        print(','.join(str(x) for x in result))
    else:
        update_index()

