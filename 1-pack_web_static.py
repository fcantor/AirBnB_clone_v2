#!/usr/bin/python3
'''Fabric script that generates a tgz archive of the web_static contents'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''Packs files'''
    local('mkdir -p versions')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local('tar cvfz versions/web_static_' + timestamp + '.tgz web_static')
