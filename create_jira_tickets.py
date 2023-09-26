import sys
import requests
from jinja2 import Template

# Define your Jira API URL and credentials
#jira_url = 'https://your-jira-instance.atlassian.net/rest/api/3/issue'
#username = 'your-username'
#api_token = 'your-api-token'

# Jira API URL
base_url = "https://abheetha-ishan.atlassian.net"
api_url = f"{base_url}/rest/api/3/issue"
general_template = "templates/general_jira_ticket_template.j2"
okra_template = "templates/okra_jira_ticket_template.j2"

# Extract parameters from command-line arguments
jira_username = sys.argv[1] 
jira_api_token = sys.argv[2]
template_type = sys.argv[3]

if template_type == "GENERAL":
    j2_template = general_template
else:
    j2_template = okra_template

# Load the Jinja2 template
with open(j2_template, 'r') as template_file:
    template_content = template_file.read()
jinja_template = Template(template_content)

if template_type == "GENERAL":
    # Extract parameters from command-line arguments
    project = sys.argv[4]
    summary = sys.argv[5]
    jira_parent_id = sys.argv[6]
    jira_assignee_id = sys.argv[7]
    goal = sys.argv[8]
    value = sys.argv[9]
    description = sys.argv[10]
    acceptance_criteria = sys.argv[11]
    
    # Create the ticket data dictionary
    ticket_data = {
        "project": project,
        "summary": summary,
        "jira_parent_id": jira_parent_id,
        "jira_assignee_id": jira_assignee_id,
        "goal": goal,
        "value": value,
        "description": description,
        "acceptance_criteria": acceptance_criteria
    }
else:
    # Extract parameters from command-line arguments
    project = sys.argv[4]
    summary = sys.argv[5]
    jira_parent_id = sys.argv[6]
    jira_assignee_id = sys.argv[7]
    goal = sys.argv[8]
    value = sys.argv[9]
    description = sys.argv[10]
    #acceptance_criteria = sys.argv[11]
    
    # Create the ticket data dictionary
    ticket_data = {
        "project": project,
        "summary": summary,
        "jira_parent_id": jira_parent_id,
        "jira_assignee_id": jira_assignee_id,
        "goal": goal,
        "value": value,
        "description": description,
        #"acceptance_criteria": acceptance_criteria
    }

# Render the Jinja2 template
ticket_json = jinja_template.render(ticket_data)

# Create and send the ticket
response = requests.post(
    api_url,
    json=ticket_json,
    auth=(jira_username, jira_api_token),
    headers={'Content-Type': 'application/json'}
)

if response.status_code == 201:
    print(f"Ticket created successfully: {response.json()['key']}")
else:
    print(f"Failed to create ticket: {response.status_code}, {response.text}")
