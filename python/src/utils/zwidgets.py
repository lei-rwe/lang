import os
import logging
from logging.config import fileConfig
from logging import FileHandler

print('zwidgets:', os.getcwd())
print('zwidgets:', __file__)

def _make_logger():
    # Assume the configure file is at the same level of this file
    full_path = os.path.realpath(__file__)
    d1 = os.path.dirname(full_path)
    d2 = os.path.dirname(d1)
    log_conf_file = os.path.join(d2, 'conf', 'zlog.ini')
    fileConfig(log_conf_file)
    print('Loaded log configuration file ' + log_conf_file)

    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, FileHandler):
            print('Logging to file {}'.format(handler.baseFilename))

    return logger

mylogger = _make_logger()
