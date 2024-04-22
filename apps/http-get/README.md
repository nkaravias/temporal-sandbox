# Temporal Python http-get Application

This repository contains a Temporal workflow application written in Python that demonstrates how to perform a series of activities including navigating a filesystem, cloning a Git repository, listing files, and making an HTTP GET request.

## Project Structure

The application is structured as follows:

- `activities.py`: Implements the activities used by the workflow.
- `workflow.py`: Defines the workflow logic that orchestrates the execution of activities.
- `worker.py`: Hosts the worker service that polls Temporal for tasks and executes workflows and activities.
- `client.py`: Starts the workflow execution.

## Prerequisites

Before running the application, ensure you have the following installed on your system:
- Python 3.8 or higher
- Git
- Docker (for running Temporal server locally)

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nkaravias/temporal-sandbox.git
   cd apps/http-get
   ```
2. **Create a virtual env**
python -m venv venv
source venv/bin/activate

3. **Install requirements**
pip install -r requirements.txt

4. **Running the Application**
Start the Worker
Run the worker script to listen for tasks from the Temporal server:
    ```bash
      python worker.py
    ```
Start the Workflow
Execute the client script to start the workflow:
    ```bash
       python client.py
    ```
This script triggers the workflow that performs the series of defined activities.

5. **Workflow Activities**
The workflow includes the following activities:

Navigate to a specified path in the filesystem.
Execute a git clone command to clone a specified repository.
List the file contents of the cloned repository.
Perform an HTTP GET request to a REST API hosted on http://localhost:8449.
Print the output of the API call.
