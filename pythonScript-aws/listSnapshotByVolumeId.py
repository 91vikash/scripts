'''
README
@Vikash


This script will list all the snapshots associated with a Volume Id


'''



import boto
import sys
from boto import ec2
connection=ec2.connect_to_region('ap-southeast-1')
snapshots=connection.get_all_snapshots(filters={'volume-id':sys.argv})
for snaps in snapshots:
    print snaps.id,"-",snaps.start_time, "-",snaps.volume_size, "\n"

