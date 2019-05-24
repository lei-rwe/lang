import os
import logging
from logging.config import fileConfig

print('zwidgets:', os.getcwd())
print('zwidgets:', __file__)

def make_logger():
    # Assume the configure file is at the same level of this file
    full_path = os.path.realpath(__file__)
    d1 = os.path.dirname(full_path)
    d2 = os.path.dirname(d1)
    log_conf_file = os.path.join(d2, 'conf', 'zlog.ini')
    print(log_conf_file)
    fileConfig(log_conf_file)

    logger = logging.getLogger()
    logger.debug('often makes a very good meal of %s', 'visiting tourists')
    return logger

mylogger = make_logger()
