import boto3
import datetime

# Replace 'your_volume_id' with the ID of the EBS volume you want to create a snapshot for
volume_id = 'vol-056630e2dfa586d45'

# Create an EC2 client
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Create a snapshot
response = ec2.create_snapshot(
    VolumeId=volume_id,
    Description=f'Snapshot created on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
)

# Print the snapshot ID
print(f"Snapshot ID: {response['SnapshotId']}")
