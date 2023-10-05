# Update package repositories
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/local/bin', '/bin'],
  refreshonly => true,
}

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

# Create the index.html file for /data/web_static/releases/test
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Set ownership
exec { 'chown_data':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/usr/bin', '/usr/local/bin', '/bin'],
}

# Create necessary directories for the default Nginx site
file { ['/var/www', '/var/www/html']:
  ensure => 'directory',
}

# Create the index.html file for /var/www/html
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>',
}

# Configure Nginx
file { '/etc/nginx/sites-enabled/default':
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => 'running',
}

