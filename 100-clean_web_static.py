#!/usr/bin/python3
''' Delete outdated archives using do_clean '''
from fabric.api import env, run, local


env.hosts = ['35.231.33.237', '34.74.155.163']
env.user = 'ubuntu'


def do_clean(number=0):
    ''' Delete out-of-date archives
    Args:
        number (int): The number of archives to keep
    '''
    number = int(number)
    number = 2 if number == 0 else number + 1
    path = '/data/web_static/releases'
    del_cmd = 'ls -t | tail -n +{} | xargs rm -rf'.format(number)

    local('cd versions ; ' + del_cmd)
    run('cd {} ; {}'.format(path, del_cmd))
