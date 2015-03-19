'''
README

This script will update the security group of Running/Stopped Instance with the given CIDR

'''
import sys
import boto 
from boto import ec2
from boto import sns
connection=ec2.connect_to_region("us-east-1")
sg=connection.get_all_security_groups()
removeIP=['1.2.3.4/32','5.6.7.8/32','9.10.11.12/32']
allowIP=['X.X.X.X/32','Y.Y.Y.Y/32','Z.Z.Z.Z/32']
for securityGroup in sg:
    global instanceId;
    
    for instanceid in securityGroup.instances():
        instanceId=str(instanceid)
			
	for ri in removeIP:
		print "Revoking Port 22 access from IP: %s from SecurityGroup: %s" %(ri,securityGroup.name) 
		securityGroup.revoke(ip_protocol='tcp',from_port=22,to_port=22,cidr_ip=ri)

	for ai in allowIP:

		print "Allowing Port 22 access from IP : %s in SecurityGroup : %s " %(ai,securityGroup.name)

		securityGroup.authorize(ip_protocol='tcp',from_port=22,to_port=22,cidr_ip=ai)


        print "-----------------------------**************************************************************-------------------------"


