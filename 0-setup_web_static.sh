#!/usr/bin/env bash
# Prepares the web server for deployment of a static web page
apt-get update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Test HTML Text" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
SRC=https://raw.githubusercontent.com/stephenchu530/AirBnB_clone_v2/master/default
DST=/etc/nginx/sites-available/default
wget $SRC -O $DST
service nginx restart
