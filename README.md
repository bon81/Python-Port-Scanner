# Python-Port-Scanner

## Overview
This is a simple but effective multi-threaded port scanner written in Python. It scans a given IP or hostname for open ports and logs the results. The goal was to keep it lightweight and easy to use while incorporating multi-threading for faster scanning.



## Features
- **Multi-threaded scanning** for improved speed.
- **Identifies open ports** and their associated services.
- **Logs scan results** to a file (`scan_results.log`).
- **Handles common errors** like invalid hostnames and connection timeouts.


## Installation
### Prerequisites
- Python 3.6+

### Setup
**Please note:** Only Step 1 is required to use the port scanner, the following steps are if you wish to use the TDD suite.

1. Clone the repo:
   ```bash
   git clone https://github.com/bon81/Python-Port-Scanner.git
   cd Python-Port-Scanner 
   ```
2. Create and activate a virtual enviroment(optional but reccomended)
    ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    export PYTHONPATH=$(pwd)
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage 
Run the script with a target hostname or IP address:
```bash
python src/port_scanner.py <target>
```
Example:
```bash
python src/port_scanner.py example.com
```
The script scans common ports(1-1023) and creates the document `scan_results.log` to store a log of the results.


## Running Tests
To run tests:
```bash
pytest
```
To check test coverage:
```bash
pytest --cov=src --cov-report=term-missing
```