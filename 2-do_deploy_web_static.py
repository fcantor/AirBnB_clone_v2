#!/usr/bin/python3
'''
Script that generates a .tgz archive from the contents of the web_static folder
'''
from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['35.231.160.140', '35.231.83.167']
env.user = 'ubuntu'


def do_pack():
    '''Generates a .tgx archive'''
    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    '''Script that distributes an archive to your web servers'''
    if not exists(archive_path) and not isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp')
        filename = archive_path.split('/')[:-4]
        run('sudo mkdir -p /data/web_static/releases/' + filename + '/')
        run('sudo chown -R ubuntu:ubuntu /data')
        run('tar -xzf /tmp/' + filename + '.tgz'
            ' -C /data/web_static/releases/' + filename + '/')
        run('rm /tmp/' + filename + '.tgz')
        run('mv /data/web_static/releases/' + filename + '/web_static/*' +
            'data/web_static/releases' + filename + '/')
        run('rm -rf /data/web_static/releases/' + filename + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/' + filename + '/' +
            '/data/web_static/current')
        return True
    except:
        return False
    return True

if __name__ == "__main__":
    do_pack()
