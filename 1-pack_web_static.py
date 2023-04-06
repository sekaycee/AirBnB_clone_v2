#!/usr/bin/python3
''' Form a tarball from web_static and download to versions '''
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    ''' Create a tarball of the directory web_static '''
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
