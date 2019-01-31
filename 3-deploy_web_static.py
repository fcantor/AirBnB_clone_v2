#!/usr/bin/python3
'''
Script that generates a .tgz archive from the contents of the web_static folder
'''
from fabric.operations import local, run, put, env
from datetime import datetime
import os


env.hosts = ['35.231.160.140', '35.231.83.167']
env.user = "ubuntu"


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
    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    filename = archive_path[9:]
    foldername = "/data/web_static/releases/" + filename[:-4]
    filename = "/tmp/" + filename
    if not run("mkdir -p {}".format(foldername)).succeeded:
        return False
    if not run("tar -xzf {} -C {}".format(filename, foldername)).succeeded:
        return False
    if not run("rm {}".format(filename)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(foldername,
                                              foldername)).succeeded:
        return False
    if not run('rm -rf {}/web_static'.format(foldername)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(
        foldername)).succeeded


def deploy():
    '''Script that creates and distributes an archive to your web servers'''
    pkg = do_pack()
    if pkg is False:
        return False
    return do_deploy(pkg)


if __name__ == "__main__":
    do_deploy()
