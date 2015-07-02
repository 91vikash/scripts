


######################################## THIS SCRIPT WILL CALCULATE THE SIZE OF S3 BUCKET  ########################################


### Usage 



#    python  calculateSizeOfBucket.py bucketName

import boto
import sys
connection=boto.connect_s3()
bucketName=connection.lookup(sys.argv[1])
print bucketName
sizeInBytes=0

if bucketName:
    for key in bucketName:
        sizeInBytes+= key.size

        sizeInKB=sizeInBytes/1024
        print "Bucket Size in KB : " , sizeInKB



        sizeInMB=sizeInKB/1024
        print "Bucket Size in MB : " , sizeInMB



        sizeInGB=sizeInMB/1024
        print "Bucket Size in GB : " , sizeInGB

else:

    print "Please input Bucket Name."
    print "Usage :: python  calculateSizeOfBucket.py bucketName "

