#!/usr/bin/env bash

# Install Nginx if it's not already installed
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing purposes
echo "<html><head><title>Test</title></head><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link and update Nginx configuration
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo sed -i '33i\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
exit 0
