import logging
import logging.config
import pathlib
import config
import split

"""
This script is intentended to process new data and transfer them into
the archive directory.
"""

# Logger configuration
p = pathlib.Path(__file__).resolve()
p = pathlib.Path(p.parent, 'logging.conf')
logging.config.fileConfig(p)
logger = logging.getLogger(__name__)
logger.info('Arch update script has been invoked...')

# Is there a rec file inside the working directory?
logger.debug('Going to look for *.rec files...')
files = list(config.WORK_PATH.glob('*.rec'))
if len(files) == 1:
    logger.debug('There is one rec file in the work directory')
elif len(files) > 1:
    logger.debug('There are rec files in the working directory')
else:
    logger.debug('The is not any rec file in the working directory')
for f in files:
    pass

# Is there a csv file inside the working direstory?
logger.debug('Going to look for *.rec files...')
files = list(config.WORK_PATH.glob('*.csv'))
for f in files:
    logger.debug(f)
    split.split(f)
