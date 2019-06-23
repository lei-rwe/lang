import logging

import conf.env_config as conf


def lib_method():
    E = conf.E
    logging.info('In lib_method: info')
    logging.warning('In lib_method: warning')
    print(E)


if __name__ == '__main__':
    conf.env_config()
    lib_method()