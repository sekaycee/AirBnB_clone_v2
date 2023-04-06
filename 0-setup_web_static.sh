#!/usr/bin/env bash
# Set up your web servers for the deployment of 'web_static'

apt -y update
apt -y install nginx
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo 'HBNB Webserver Test' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
