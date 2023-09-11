import requests
import json
import csv
import sys

# Jira API URL
base_url = "https://abheetha-ishan.atlassian.net"
api_url = f"{base_url}/rest/api/2/issue/bulk"

# Replace with your Jira username and API token
username = str(sys.argv[2])
api_token = str(sys.argv[3])

# Create a session to store authentication credentials
session = requests.Session()
session.auth = (username, api_token)

# Read issues data from a CSV file
csv_file = str(sys.argv[1])  # Replace with your CSV file path
issues = []

with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        issue = {
            "fields": {
                "project": {
                    "key": row['Project']
                },
                "summary": row['Summary'],
                "issuetype": {
                    "name": row['IssueType']
                },
                "assignee": {
                    "name": row['Assignee']  # Use email address as assignee
                },
                "description": row['Description']
                # Add more fields as needed
            }
        }
        print(f'Creating issue: {json.dumps(issue, indent=2)}')
        issues.append(issue)

# Create the bulk issue payload
payload = {
    "issueUpdates": issues
}

# Send a POST request to create the bulk issues
response = session.post(api_url, json=payload)

if response.status_code == 201:
    print("Bulk issues created successfully!")
else:
    print(f"Failed to create bulk issues. Status code: {response.status_code}")
    print(response.text)
