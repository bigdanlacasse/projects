class gw2ch {
  exec { "apt-get update":
    command => "sudo apt-get update"
  }

  $packages = [
    "ack",
    "vim",
    "curl",
    "tmux",
    "git",
    "nginx",
    "varnish",
    "php5",
    "php5-cli",
    "php5-fpm",
    "php5-curl",
    "php5-mysql",
    "php5-memcache",
    "php5-gd",
    "php-pear",
    "redis-server",
    "memcached",
    "mysql-server",
	"python-setuptools"
  ]

  package {
    $packages: ensure => "installed",
    require => Exec["apt-get update"]
  }

  $password = "testtest321"
  exec { "mysql root password":
    require => Package["mysql-server"],
    unless => "mysqladmin -uroot -p$password status",
    command => "mysqladmin -uroot password $password",
  }

  exec { "setup-project-database":
    #command => "mysqladmin -uroot -p$password create gw2spidy; mysql -uroot -p$password gw2ch < config/schema.sql",
	command => "mysqladmin -uroot -p$password create gw2ch;",
    cwd => "/vagrant",
    require => Exec["mysql root password"]
  }

  exec { "pear-channel-discovery":
    command => "sudo pear channel-discover pear.phing.info",
    require => Package["php-pear"],
    onlyif => "test `pear list-channels | grep 'pear.phing.info' | wc -l` -eq 0"
  }

  exec { "fetch-php-extensions":
    command => "sudo pear install phing/phing Log",
    require => Exec["pear-channel-discovery"]
  }

  service { 'nginx':
      ensure => running,
      require => Package['nginx']
  }

  service { 'varnish':
    ensure => running,
    require => Package['varnish']
  }

  service { 'redis-server':
    ensure => running,
    require => Package['redis-server']
  }

  service { 'memcached':
    ensure => running,
    require => Package['memcached']
  }

  service { 'mysql':
    ensure => running,
    require => Package['mysql-server']
  }

  service { 'php5-fpm':
      ensure => running,
      require => Package['php5-fpm']
  }

}