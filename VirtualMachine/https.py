import http.client

# Replace with your EC2 instance's public DNS name or IP address
ec2_instance_host = '16-16-28-248'

# Make an HTTPS request to your EC2 instance
conn = http.client.HTTPSConnection(ec2_instance_host)

# Specify the path and method (GET, POST, etc.)
path = '/'
method = 'GET'

# Send the request
conn.request(method, path)

# Get the response
response = conn.getresponse()

# Print the response status code
print(f'Status Code: {response.status}')

# Print the response body
response_data = response.read()
print(f'Response Body: {response_data.decode("utf-8")}')

# Close the connection
conn.close()
