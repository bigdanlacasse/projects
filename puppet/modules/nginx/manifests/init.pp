class nginx {
  file { 'vagrant-nginx':
      path => '/etc/nginx/sites-available/gw2ch',
      ensure => file,
      require => Package['nginx'],
      source => 'puppet:///modules/nginx/gw2ch.txt',
  }

  file { 'default-nginx-disable':
      path => '/etc/nginx/sites-enabled/default',
      ensure => absent,
      require => Package['nginx'],
  }

  file { 'vagrant-nginx-enable':
      path => '/etc/nginx/sites-enabled/vagrant',
      target => '/etc/nginx/sites-available/gw2ch',
      ensure => link,
      notify => Service['nginx', 'php5-fpm'],
      require => [
          File['vagrant-nginx'],
          File['default-nginx-disable'],
      ],
  }
}