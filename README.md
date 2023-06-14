# Files2JSON

This is a Python program that converts CSV, XML, or HTML files into JSON format. The program takes a file input, performs a conversion, and outputs a JSON file that can then be used for various purposes.

## Getting Started

### Prerequisites

Before running the program, make sure that you have Python 3 installed on your computer:

## Download and Install Python 3 on Ubuntu
```
sudo apt install python3
```

### Verify Python3 is installed correctly
```
python3 --version
```

The output should show the Python version number (e.g. Python 3.9.5).


# Installation

To get started, you can download the program from the Github page:

### Download Files2JSON

After you have downloaded the program, navigate to the `Files2JSON` folder using the terminal/command prompt and execute the following command:
```
python setup.py
```

This command will install the necessary Python dependencies and create the directory structure required by the program.

### Usage

To perform a conversion, simply execute the following command in the terminal:
```
python csv_to_json.py
```

When prompted, enter the path and filename of the file you want to convert.

The program will then convert the file based on its type and save it in the `output_files` directory located in the same folder as `csv_to_json.py`.

### Troubleshooting

If the program encounters any issues, check the following:

- Make sure that you have the Python dependencies installed by running `pip install -r requirements.txt`
- Make sure that the input file exists in the `input_files` directory
- Check the file permissions to ensure that the program has permission to read/write files
- If you encounter any issues that you cannot solve, please feel free to open an issue on the Github page. We'll be happy to help you troubleshoot the problem.

## Acknowledgements

Thank you for using Files2JSON! We appreciate your support and welcome any feedback you might have.



