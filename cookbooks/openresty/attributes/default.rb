default['openresty']['version'] = '1.9.7.4'
default['openresty']['name'] = 'openresty'
default['openresty']['url'] = "https://openresty.org/download/#{node['openresty']['name']}-#{node['openresty']['version']}.tar.gz"
default['openresty']['dir'] ='/etc/nginx/'
default['openresty']['logdir'] ="/var/log/nginx/"
default['openresty']['keepalive'] = 'on'
default['openresty']['cpu'] = 'node["cpu"]["total"]'
default['openresty']['tempPath']= Chef::Config['file_cache_path'] || '/tmp'
default['openresty']['worker_connections'] = node["cpu"]["total"].to_i * 1024