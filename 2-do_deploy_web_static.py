#!/usr/bin/python3
'''Fabric script that distributes an archive to a remote server'''
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['35.185.114.101', '35.185.47.103']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'


def do_deploy(archive_path):
    '''Deploys archive web servers'''
    if exists(archive_path):
        put(archive_path, '/tmp')
        filename = archive_path.split('/')[1][:-4]
        run('mkdir -p /data/web_static/releases/' + filename + '/')
        run('tar -xzf /tmp/' + filename + '.tgz'
            ' -C /data/web_static/releases/' + filename + '/')
        run('rm /tmp/' + filename + '.tgz')
        run('mv /data/web_static/releases/' + filename + '/web_static/* ' +
            '/data/web_static/releases/' + filename + '/')
        run('rm -rf /data/web_static/releases/' + filename + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/' + filename + '/ ' +
            '/data/web_static/current')
    else:
        return False
    return True
