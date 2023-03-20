import boto3
import json
import sys

# configure your ssm client here, such as AWS key or region

session = boto3.Session(profile_name='personal-aws-account')

# us-east-1 - N. Virginia
# us-east-2 - Ohio
# us-west-1 - N. California
# us-west-2 - Oregon
ssm_client = session.client('ssm',
    region_name="us-east-2"
)

json_file = 'example.json'
#path prefix for SSM Parameter - eg. /cluster, the final result would be /cluster/app/VAR_NAME
path_prefix = ""
  
# JSON file
f = open (json_file, "r")
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
for i in data['Parameters']:
    try:
        name = path_prefix+i['Name']
        value = i['Value']
        var_type = i['Type']

        print(name)
        print(value)
        print(var_type)
        print('######################')
        response = ssm_client.put_parameter(
            Name=name,
            Value=value,
            Type=var_type,
            Overwrite=False
        )
        print(response)
        print('######################')
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()

# Closing file
f.close()
