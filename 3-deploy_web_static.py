#!/usr/bin/python3
''' Create and distribute an archive to a web server using deploy '''
from datetime import datetime
from fabric.api import env, put, run, local
import os

env.hosts = ['54.90.40.0', '54.90.23.41']
env.user = 'ubuntu'

def do_pack():
    try:
        if not os.path.exists('versions'):
            os.mkdir('versions')
        t = datetime.now()
        f = '%Y%m%d%H%M%S'
        tb_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(tb_path))
        return tb_path
    except Exception:
        return None


def do_deploy(archive_path):
    ''' Deploy the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    '''
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        dir_name = file_name.replace('.tgz', '')
        releases_path = '/data/web_static/releases/{}/'.format(dir_name)
        tmp_path = '/tmp/' + file_name

        put(archive_path, tmp_path)
        run('mkdir -p ' + releases_path)
        run('tar -xzf {} -C {}'.format(tmp_path, releases_path))
        run('rm ' + tmp_path)
        run('mv {}web_static/* {}'.format(releases_path, releases_path))
        run('rm -rf {}web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except Exception:
        return False

def deploy():
    ''' Create and distribute an archive to a web server '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
