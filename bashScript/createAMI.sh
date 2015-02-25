#!/bin/bash


_instanceIDS="instanceIDS " # Put Instance ID separated by space

_date=`date +"%m-%B-%Y"`


for instanceID in ${_instanceIDS[@]};do

        # Get the Tag Associated with the EC2 Instances
       _tag=$(aws ec2 describe-instances  --filters "Name=instance-id,Values=$instanceID " --query Reservations[*].Instances[*].Tags[*].Value --output text)
     
        
      echo "Creating AMI for $_tag Instance having instance ID : $instanceID"
      
      aws ec2 create-image --instance-id $instanceID --description $_tag-AMI-$_date --no-reboot 
done
