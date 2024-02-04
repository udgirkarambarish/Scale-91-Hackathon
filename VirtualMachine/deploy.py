import subprocess
import os

# Replace 'your-ec2-public-ip' and 'your-local-codebase-path' with actual values
ec2_ip = '3.108.217.49'
local_path = r'C:\Users\mrunm\Desktop\awsPy\spacehakethon'
private_key_path = r'C:\Users\mrunm\Desktop\awsPy\ec2.pem'

# Ensure that only the owner has read and write permissions on the private key
os.chmod(private_key_path, 0o600)

# Define the command to execute
scp_command = [
    'scp', '-i', private_key_path,
    '-r', local_path,
    f'ec2-user@{ec2_ip}:/home/ec2-user/'
    ]

# Run the command
subprocess.run(scp_command)
