

#!/bin/bash
import xlwt  #To create a workseet

import boto
from boto import ec2

workBook = xlwt.Workbook(encoding="utf-8")
sheet	 = workBook.add_sheet("List of All Instances")



#Apply Style to the sheet

pattern = xlwt.Pattern() # Create the Pattern 

pattern.pattern = xlwt.Pattern.SOLID_PATTERN 

pattern.pattern_fore_colour = 3

style = xlwt.XFStyle() 

style.pattern = pattern 


#Apply the width to the Column

for width in range(0,3):
	sheet.col(width).width=7777


connection=ec2.connect_to_region("ap-southeast-1"); #Connect to ap-southeast-1 region 

reservations=connection.get_all_instances(); #Get All Reservation Id


# Get the list of All Instance Name
def getAllInstanceTags(reservations):
	x=0
	y=0

	
	sheet.write(x,y,"InstanceName",style)
	sheet.write(x,y+1,"IP Address",style)
	sheet.write(x,y+2,"Instance Class",style)

	x=x+1

	for reservation in reservations:
		for instance in reservation.instances:
			
			if 'Name' in instance.tags:
				#print instanceId.tags['Name']
				sheet.write(x,y,instance.tags['Name'])
				sheet.write(x,y+1,instance.ip_address)
				sheet.write(x,y+2,instance.instance_type)
				x=x+1					
				
			else: 
				print "%s %s" %(instance.id,instance.state)


getAllInstanceTags(reservations)	


#Sort Column Instance Name


workBook.save("InstanceDetails.xls")


