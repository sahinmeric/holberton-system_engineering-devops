# Increases the open file limit for nginx

exec { 'Increase limit':
    command  => 'sed -i "s/-n 15/ -n 50000/g" /etc/default/nginx',
    provider => 'shell'
}

exec { 'Restart nginx':
    command  => 'sudo service nginx restart',
    provider => 'shell'
}
