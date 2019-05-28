import os
print('python/src/__init__.py: Setup running environment')


def _setup_running_env():
    print('python/src/__init__.py:', os.getcwd())
    print('python/src/__init__.py:', __file__)

    cwd = os.getcwd()

    # log directory should be at the same level of 'src'
    logdir = os.path.dirname(os.path.dirname(__file__))
    log_1 = os.path.join(logdir, 'log')
    log_2 = os.path.join(logdir, 'logs')
    if os.path.isdir(log_1):
        logdir = log_1
    elif os.path.isdir(log_2):
        logdir = log_2
    print(logdir)

    if 'ZLOGDIR' not in os.environ:
        os.environ['ZLOGDIR'] = logdir

_setup_running_env()
