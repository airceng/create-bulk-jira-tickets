import csv
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# logging.error("Error Logging")
# logging.info("Info Logging")

# Define a function to validate the CSV file
def validate_csv(file_path):
    try:
        # Open the CSV file for reading
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)

            # Check if the CSV file has a header row
            header = next(reader, None)
            if header is None:
                print("Error: CSV file has no header row.")
                return False

            # Define your validation rules here
            # For example, check if the header contains the expected columns
            expected_columns = ['Project', 'Summary', 'IssueType', 'Assignee', 'Description']
            if header != expected_columns:
                print("Error: Unexpected columns in the CSV header.")
                return False

            # You can add more validation checks here, such as data type validation,
            # data range validation, and so on.

            # If all checks pass, the CSV file is valid
            print("CSV file is valid.")
            return True

    except FileNotFoundError:
        print("Error: File not found.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

# Example usage:
#if validate_csv('outputs.csv'):
if validate_csv(str(sys.argv[1])):
    # Process the CSV file if it's valid
    pass
else:
    # Handle validation errors
    pass
