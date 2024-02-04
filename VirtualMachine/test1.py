import boto3

aws_management_console = boto3.session.Session(profile_name = 'default')
ec2_console = aws_management_console.client('ec2')

# Specify your instance ID
instance_id = 'i-0633ec4f43523c747'

# Describe the instance to get its public DNS name or IP address
response = ec2_console.describe_instances(InstanceIds=[instance_id])
instance_info = response['Reservations'][0]['Instances'][0]
public_dns = instance_info['PublicDnsName']
print(public_dns)
