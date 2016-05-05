#
# Cookbook Name:: open-Recipe
# resty:: default
#
# Copyright 2016, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#


#Installing prerequisite

execute 'Updating apt-get' do 

	user 'root'
	command "apt-get update"
	end


# Dependencie Installation
package 'libreadline-dev' do 
	action :install
end

package 'libncurses5-dev' do
	action :install
end

package	'libpcre3-dev' do
	action :install
end

package 'libssl-dev' do
	action :install
end

package 'perl' do 
	action :install
end

package 'make' do
	action :install
end

package 'build-essential' do
	action :install
end



filename = "#{node['openresty']['tempPath']}/#{node['openresty']['name']}-#{node['openresty']['version']}.tar.gz"


# Download the openresty package
remote_file node['openresty']['url'] do
	source node['openresty']['url']
	path filename
	end


# Install 

bash 'Install openresty' do

	cwd ::File.dirname(filename)

	code <<-EOH
		tar -xvf #{::File.basename(filename)} -C #{::File.dirname(filename)} &&
		cd #{node['openresty']['name']}-#{node['openresty']['version']} &&
		./configure --prefix=/opt/openresty --user=www-data --group=www-data --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --pid-path=/var/run/nginx.pid  --with-pcre --with-pcre-jit --with-luajit --with-http_ssl_module
		make && make install

	EOH
end


#Create Nginx Service

template '/etc/init.d/nginx' do 
	source 'nginx.init.erb'
	mode '0777'
end



service 'nginx' do 
	action :start
end
