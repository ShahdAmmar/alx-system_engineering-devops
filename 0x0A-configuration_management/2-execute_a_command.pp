# killing a process called killmenow
exec { 'pkill killmenow':
        path => '/usr/bin:/usr/sbin:/bin',
}
