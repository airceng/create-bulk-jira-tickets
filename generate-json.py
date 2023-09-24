import sys
import json
from jinja2 import Template
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

OKRA_TEMPLATE_NAME = "template/okra-template.json.j2"
GENERAL_TEMPLATE_NAME = "template/general-template.json.j2"

# Check template type
if str(sys.argv[1]) == OKRA_TEMPLATE_NAME:
    if len(sys.argv) != 7:
        print("Usage: python script.py <template_file> <project_user_details_json> <summary> <jira_parent_id> <goal> <value>")
        logging.error("Invalid arguments for OKRA")
        sys.exit(1)

if str(sys.argv[1]) == GENERAL_TEMPLATE_NAME:
    if len(sys.argv) != 9:
        print("Usage: python script.py <template_file> <project_user_details_json> <summary> <jira_parent_id> <goal> <value> <description> <acceptance_criteria>")
        logging.error("Invalid arguments for GENERAL")
        sys.exit(1)

# Read the Jinja2 template from the specified file
template_file_path = sys.argv[1]
with open(template_file_path, 'r') as template_file:
    template_str = template_file.read()

# Create a Jinja2 template object
template = Template(template_str)

# Read the JSON input from the specified file
json_file_path = sys.argv[2]
with open(json_file_path, 'r') as json_file:
    project_user_details = json.load(json_file)

# Iterate over the list of project_user_details and render the template for each combination
for item in project_user_details:
    project, jira_assignee_id = item

    if str(sys.argv[1]) == OKRA_TEMPLATE_NAME:
        variables = {
            "project": project,
            "summary": str(sys.argv[3]),
            "jira_parent_id": str(sys.argv[4]),
            "jira_assignee_id": jira_assignee_id,
            "goal": str(sys.argv[5]),
            "value": str(sys.argv[6])
        }

    if str(sys.argv[1]) == GENERAL_TEMPLATE_NAME:
        variables = {
            "project": project,
            "summary": str(sys.argv[3]),
            "jira_parent_id": str(sys.argv[4]),
            "jira_assignee_id": jira_assignee_id,
            "goal": str(sys.argv[5]),
            "value": str(sys.argv[6]),
            "description": str(sys.argv[7]),
            "acceptance_criteria": str(sys.argv[8])
        }

    # Render the template with the current variable values
    result_json = template.render(**variables)
    print(result_json)

    # Define the output JSON file name
    output_file_name = f"{project}_{jira_assignee_id}.json"

    # Write the generated JSON to the output file
    with open(output_file_name, 'w') as output_file:
        json.dump(json.loads(result_json), output_file, indent=2)

    print(f"Generated JSON for Project: {project}, Assignee ID: {jira_assignee_id}, Saved to {output_file_name}")
