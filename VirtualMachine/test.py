from flask import Flask, request, jsonify, render_template
import pandas as pd
import boto3
import logging
from datetime import datetime

app = Flask(__name__)

# Load existing Excel file or create a new DataFrame if the file doesn't exist
excel_filename = 'user_log.xlsx'
try:
    df = pd.read_excel(excel_filename)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Action', 'Target', 'Timestamp', 'Coordinates', 'browser', 'browserVersion', 'microtime', 'scrnRes', 'ipAddress', 'url', 'starttime', 'endtime', 'modifiers'])

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create CloudWatch Logs client
cloudwatch_logs = boto3.client('logs', region_name='ap-south-1')  # Replace 'your_region' with your AWS region

# Create a log group if it doesn't exist
log_group_name = 'kali-testing'
try:
    cloudwatch_logs.create_log_group(logGroupName=log_group_name)
except cloudwatch_logs.exceptions.ResourceAlreadyExistsException:
    pass  # Log group already exists

# Create a log stream with a timestamp
log_stream_name = f'LogStream_{datetime.utcnow().isoformat()}'
cloudwatch_logs.create_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/api/log', methods=['POST'])
def log_endpoint():
    global df  # Use the global DataFrame

    data = request.json
    user_log = {}

    Action = data.get('action')
    user_log['Action'] = Action
    Target = data.get('target')
    user_log['Target'] = Target
    Timestamp = data.get('timestamp')
    user_log['Timestamp'] = Timestamp
    Coordinates = data.get('coordinates')
    user_log['Coordinates'] = Coordinates
    browser = data.get('browser')
    user_log['browser'] = browser
    browserVersion = data.get('browserVersion')
    user_log['browserVersion'] = browserVersion
    microtime = data.get('microtime')
    user_log['microtime'] = microtime
    scrnRes = data.get('screenResolution')
    user_log['scrnRes'] = scrnRes
    ipAddress = data.get('ipAddress')  # Corrected the variable name
    user_log['ipAddress'] = ipAddress
    url = data.get('currentURL')
    starttime = data.get('starttime')
    endtime = data.get('endtime')
    user_log['starttime'] = starttime
    user_log['endtime'] = endtime
    modifiers = data.get('modifiers')
    user_log['modifiers'] = modifiers
    user_log['url'] = url
    print(modifiers)

    # Append the new user log to the DataFrame
    df = pd.concat([df, pd.DataFrame([user_log])], ignore_index=True)

    # Send log entry to CloudWatch Logs
    log_message = ','.join([f'{key}={value}' for key, value in user_log.items()])
    cloudwatch_logs.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': int(datetime.utcnow().timestamp() * 1000),
                'message': log_message,
            },
        ]
    )
    logger.info(f'Sent log entry to CloudWatch Logs: {log_message}')

    # Save the DataFrame to the Excel file
    df.to_excel(excel_filename, index=False, sheet_name='Sheet1', engine='openpyxl')

    return jsonify({'status': 'success'})

@app.route('/api/get_analysis')
def get_analysis():
    # Fetch CloudWatch analysis data (replace this with your actual logic)
    analysis_data = {'metric1': 123, 'metric2': 456, 'metric3': 789}
    return jsonify(analysis_data)



if __name__ == '__main__':
    app.run(debug=True)
