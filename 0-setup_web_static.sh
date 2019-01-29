#!/usr/bin/env bash
# Sets up web servers for deployment
FILE=/etc/nginx/sites-available/default
STRING="location /hbnb_static/ {\nalias /data/web_static/current/; \n}\n"
HTML="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo -e "$HTML" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "39i $STRING" $FILE
sudo service nginx restart
