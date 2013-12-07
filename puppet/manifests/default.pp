# Basic Puppet Apache manifest
class apache {
  exec { 'apt-get update':
    command => '/usr/bin/apt-get update'
  }

  package { "apache2":
    ensure => present,
  }

  service { "apache2":
    ensure => running,
    require => Package["apache2"],
  }

  file { '/var/www':
    ensure => link,
    target => "/vagrant/site",
    notify => Service['apache2'],
    force  => true
  }
}

include apache

# PHP
# https://github.com/experience/vagrant-puppet-php
class php {
  if ! defined(Package['php5']) {
    package { 'php5':
      ensure => 'present',
    }
  }

  file { 'php.ini':
    ensure  => 'file',
    path    => '/etc/php5/apache2/php.ini',
    source  => '/php.ini',
    require => Package['php5'],
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
  }
}
include php


# MySQL
# https://github.com/experience/vagrant-puppet-mysql
include '::mysql::server'

class { '::mysql::server': 
	root_password => 'd1e9c6e9##',
	bind_address => '192.168.56.101',
}

mysql_database { 'devdb':
  ensure  => 'present',
  charset => 'utf8'
}

database_user { 'dlacasse@%':
  password_hash => mysql_password('testtest321')
}

database_grant { 'dlacasse@%/database':
  privileges => ['all'] ,
}