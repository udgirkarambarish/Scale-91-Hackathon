import boto3

# Create an EC2 client
ec2 = boto3.client('ec2', region_name='your-region')

# Specify the AMI ID for the image you want to use
ami_id = 'your-ami-id'

# Specify other instance details
instance_type = 't2.micro'
key_name = 'your-key-pair-name'

# Create a new EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1
)

# Print the newly created instance details
instance_id = response['Instances'][0]['InstanceId']
print(f"New EC2 instance created with ID: {instance_id}")
