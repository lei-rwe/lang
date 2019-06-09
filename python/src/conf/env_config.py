import os
import logging.config
from typing import Any, Dict, List, Union

CONFIG_ENV = {
    'STAGE':{
        'project': {
            'name': 'zprj',
            'home': os.path.join(os.path.expanduser('~'), 'git', 'lang', 'python'),
            'log': {
                'conf_dir': 'conf',
                'conf_file': 'logging.ini'   # default log configure file. typically project_name + '_log.ini'
            },
            'required_directories': ['conf', 'data', 'logs'],
            'env_variables': {
                'PRJ_HOME': 'project.home'
            }
        },
    }
}

def _flatten_cfg(cfg: Dict[str, Any]) -> Dict[str, Union[str, int, List[int], List[str]]]:
    '''
    reduce a multi level dict to a single level dict; concat keys to value(s)

    :param cfg: structure to be decomposed / flattened out
    :type cfg: dictionary; optional - dict of dict... / lists / tuples ....
    :returns: flattened structure dictionary with composite keys, seperated with .
    '''

    def _items():
        for key, value in cfg.items():
            if isinstance(value, dict):
                yield from ((key + "." + subkey, subvalue)
                for subkey, subvalue in _flatten_cfg(value).items())
            else:
                yield (key, value)
    return dict(_items())

def configure_logging(log_conf_file=None, log_conf_dir=None):
    # Since logging is global, need ONLY to configure it
    if not log_conf_dir:
        # Assume the configure file is at the same level of this file
        full_path = os.path.realpath(__file__)
        d1 = os.path.dirname(full_path)
        log_conf_dir = os.path.dirname(d1)

    if not log_conf_file:
        log_conf_file = 'logging.ini'

    log_conf_file = os.path.join(log_conf_dir, log_conf_file)
    print('Loading log configuration file ' + log_conf_file)
    logging.config.fileConfig(log_conf_file)

    # If the name of logger is not defined, checking its parent
    handlers = logging.getLogger().handlers
    if not handlers:
        plog = logging
        while not handlers:
            plog = plog.parent
            handlers = plog.handlers

    for handler in handlers:
        if isinstance(handler, logging.FileHandler):
            print('Logging to file {}'.format(handler.baseFilename))

def env_config(token, cmdargs=None) -> Dict[str, Union[str, int, List[int], List[str]]]:
    print(f'Loading configure for environment {token} ...')

    if not cmdargs:
        E = _flatten_cfg(CONFIG_ENV[token])
    else:
        argdict = { key : value for key, value in vars(cmdargs).items() if value }
        E = _flatten_cfg(CONFIG_ENV[token])
        E.update(argdict)

    def _check_environment_variables(E):
        print('env_config.py: checking environment variables ...')
        env_startswith = 'project.env_variables.'
        for key, value in E.items():
            if key.startswith(env_startswith):
                var = key[len(env_startswith):]
                if var not in os.environ:
                    os.environ[var] = E[value]
                    print(f'Set environment variable {var}')

    def _check_folders(E):
        print('Checking folder layout ...')
        base_dir = E['project.home']
        for s_folder in E.get('project.required_directories', {}):
            folder = os.path.join(base_dir, s_folder)
            print(f'Checking folder {folder} ...')
            if not os.path.isdir(folder):
                os.makedirs(folder)

    _check_environment_variables(E)
    _check_folders(E)

    configure_logging(E['project.log.conf_file'],
                      os.path.join(E['project.home'], E['project.log.conf_dir']))

    return E


if '__main__' == __name__:
    from pprint import pprint
    pprint(env_config('STAGE'))
    logging.info('info')
    logging.debug('debug')
    logging.warning('warning')
    logging.error('error', exc_info=True)
