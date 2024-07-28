#!/usr/bin/env bash
# sets up my web server for the deployment of web_static
# install nginx
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

#create necessary directories if they don't exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#create html file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#create symbolic links
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership recursively
sudo chown -R ubuntu:ubuntu /data/

#update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^\tserver_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"

#restart Nginx
sudo service nginx restart

exit 0