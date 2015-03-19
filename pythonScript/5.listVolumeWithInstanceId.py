'''
README
@Vikash


This script will return Instance with the given attached volume


'''



import boto
from boto import ec2
connection=ec2.connect_to_region('us-east-1')
reservations=connection.get_all_instances(filters={'instance-state-name':'running'});
volumes=connection.get_all_volumes()

def attachedVolumes():
	for vol in volumes:
		if vol.attachment_state() == 'attached' :
			volumeInstances =  connection.get_all_instances(filters={'block-device-mapping.volume-id':vol.id})
			for instances in volumeInstances:
				for instance in instances.instances:
					print "Volume-ID" '-' "Instance-Id" '-' "Attached Device" "\n"
					print vol.id, '-', instance.id, '-', vol.attach_data.device

attachedVolumes()
