# setting up client SSH configuration file so
# we you can connect to a server without typing a password.
file_line { 'turning off password auth':
      ensure => present,
      path   => '/etc/ssh/ssh_config',
      line   => 'PasswordAuthentication no',
      match  => 'PasswordAuthentication yes',
    }

file_line { 'adding identity file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school'
}
