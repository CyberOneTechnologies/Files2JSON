import os

# Install dependencies from requirements.txt
os.system('pip install -r csv_to_json/requirements.txt')

# Create the necessary directory structure
os.makedirs('csv_to_json/input_files', exist_ok=True)
os.makedirs('csv_to_json/output_files', exist_ok=True)

print('Setup complete.')
