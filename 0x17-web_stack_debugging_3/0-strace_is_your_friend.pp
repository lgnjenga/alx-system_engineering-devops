# 0-strace_is_your_friend.pp

# Ensure the directory for the file exists
file { '/var/www/html':
  ensure => 'directory',
}

# Ensure the PHP file exists with correct permissions
file { '/var/www/html/index.php':
  ensure  => 'file',
  content => '<?php phpinfo(); ?>',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

# Ensure Apache service is running
service { 'apache2':
  ensure => 'running',
  enable => true,
  require => File['/var/www/html/index.php'],
}

