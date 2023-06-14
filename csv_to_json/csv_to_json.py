import pandas as pd
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json
import os.path
from datetime import datetime

# Define function to convert CSV to JSON
def csv_to_json(csv_file):
    df = pd.read_csv(csv_file)
    json_file = os.path.splitext(csv_file)[0] + '.json'
    df.to_json(json_file, orient='records')

# Define function to convert XML to JSON
def xml_to_json(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    json_file = os.path.splitext(xml_file)[0] + '.json'
    with open(json_file, 'w') as f:
        for item in root:
            f.write(json.dumps(item.attrib) + '\n')

# Define function to convert HTML to JSON
def html_to_json(html_file):
    with open(html_file) as f:
        soup = BeautifulSoup(f, 'html.parser')
    json_file = os.path.splitext(html_file)[0] + '.json'
    with open(json_file, 'w') as f:
        for item in soup.findAll('tr')[1:]:
            row = [td.text for td in item.findAll('td')]
            f.write(json.dumps(row) + '\n')

# Get user input for file name and location
input_file = input('Please enter the path and filename of the file you want to convert: ')

# Check if file exists
if not os.path.isfile(input_file):
    print('Error: File not found.')
else:
    # Get timestamp for output filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Create output filename
    output_filename = os.path.splitext(os.path.basename(input_file))[0] + '_' + timestamp + '.json'
    output_file = os.path.join('csv_to_json', 'output_files', output_filename)

    # Convert file based on file type
    if input_file.endswith('.csv'):
        csv_to_json(input_file)
    elif input_file.endswith('.xml'):
        xml_to_json(input_file)
    elif input_file.endswith('.html'):
        html_to_json(input_file)
    else:
        print(f'Error: Unsupported file type {os.path.splitext(input_file)[1]}')

    print(f'{input_file} converted successfully to {output_file}.')
