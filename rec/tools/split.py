
import re
import sys
import uuid
import config
from datetime import datetime

def get_filename():
    filename = str(uuid.uuid4())
    filename = '.'.join((filename, 'arch'))
    filename = ''.join((config.WORK_DIR, filename))
    return filename

def split(filename):

    # open given csv file for reading
    with open(filename, 'r') as infile:
        # Read header from the file
        head = list([h.strip() for h in infile.readline().split(',')])

        # Open file for writing for each variable
        files = list([None for h in head])
        for i, h in enumerate(head):
            for v in config.ARCH_VARIABLES:
                if v['archive'] and v['arch-id'] == h:
                    files[i] = open(get_filename(), 'w')
                    # write a head into the file
                    files[i].write('timestamp,{}\n'.format(h))

        # Split all of the values from stdin into the opened files
        for line in infile:
            splitted = line.split(',')
            for i, f in enumerate(files):
                if f:
                    f.write('{},{}\n'.format(splitted[0], splitted[i]))

        # Close all of the files
        for f in files:
            if f:
                f.close()

if __name__ == "__main__":
    # execute only if run as a script
    filename = sys.argv[1]
    split(filename)
