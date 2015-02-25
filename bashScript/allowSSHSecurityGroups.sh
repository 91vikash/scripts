set -e

_sec="securityGroupID"
_port=22

   echo "Adding IP 0.0.0.0/0 to Security Group $_sec"
      aws ec2 authorize-security-group-ingress --group-id $_sec --protocol tcp --port $_port --cidr "0.0.0.0/0" --region region-name


