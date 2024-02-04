import boto3

# AWS Configuration
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
region = 'your-region'  # e.g., 'us-east-1'
instance_id = 'your-ec2-instance-id'

# Initialize AWS SSM client
ssm = boto3.client('ssm', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

# Link to open on EC2 instance
link_to_open = 'https://example.com'

# Send command to open the link
command = f'start {link_to_open}'  # For Windows
response = ssm.send_command(
    InstanceIds=[instance_id],
    DocumentName="AWS-RunShellScript",
    Parameters={'commands': [command]}
)

# Print the command execution details
print(f"Command ID: {response['Command']['CommandId']}")
