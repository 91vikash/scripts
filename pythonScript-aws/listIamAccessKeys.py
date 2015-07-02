import datetime
import dateutil
from dateutil import parser

import boto
from boto import iam


conn=iam.connect_to_region('ap-southeast-1')
users=conn.get_all_users()
compareDate=""
timeLimit=datetime.datetime.now() - datetime.timedelta(days=90)

for user in users.list_users_response.users:

        if parser.parse(user['create_date']).date() <= timeLimit.date():
                    print(user['create_date']) + "\t\t" + user['user_name']

