# Configure nginx server similar to task 0 with puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install and start nginx']
}

exec {'install and start nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx && sudo service nginx start',
  before   => Exec['make directories']
}

exec {'make directories':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/ && sudo mkdir /data/web_static/shared/',
  before   => Exec['add mock html']
}

exec {'add mock html':
  provider => shell,
  command  => 'sudo echo "HBNB Webserver Test" > /data/web_static/releases/test/index.html',
  before   => Exec['create symbolic link']
}

exec {'creat symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['put location']
}

exec {'put location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart nginx']
}

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}
