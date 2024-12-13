import csv
import json

wd = 'E:/path/to/your/directory/'

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        # Convert each row into a dictionary
        data = list(csv_reader)
    
    # Write JSON data
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Specify file paths
csv_file_path = wd + 'File_Name.csv'  
json_file_path = wd + 'File_Name.json'  

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)   