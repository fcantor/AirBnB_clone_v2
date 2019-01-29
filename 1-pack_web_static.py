#!/usr/bin/python3
''' Script that generates a .tgz archive from the contents of the web_static folder'''
from fabric.operations import local
from datetime import datetime
import os


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

if __name__ == "__main__":
    do_pack()
