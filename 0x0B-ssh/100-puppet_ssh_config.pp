#!/usr/bin/env basg
# Connecting without password using Puppet

file {'/etc/ssh/ssh_config':
  ensure => present,
}

file_line {'Turning off password authentication':
  path	=> '/etc/ssh/ssh_config',
  line	=> 'PasswordAuthentication no',
}

file_line {'Declaring identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
} 
