# Increases the open file limit for nginx

exec { 'Increase limit':
    command  => 'sed -i "s/15/4096/" /etc/default/nginx',
    provider => 'shell',
}

exec { 'Restart nginx':
    command  => 'sudo service nginx restart',
    provider => 'shell'
}
