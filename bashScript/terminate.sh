_instance_id=$(aws ec2 describe-instances --query Reservations[*].Instances[*].InstanceId  --region us-east-1 --output text)

for instanceId in $_instance_id;do
	
    # If instance has Termination Policy Enabled.

    echo "Disabling Termination Policy of $instanceId"

	aws ec2 modify-instance-attribute --instance-id $instanceId --no-disable-api-termination
	

    ################ DANGER ZONE ############################
    #echo "Terminating Instances : Instance Id : $instanceId"
	
    #aws ec2 terminate-instances --instance-ids $instanceId
done

