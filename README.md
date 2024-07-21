# Flask Backup Automation Project

## Overview

This project automates the backup of files from a specific user directory on a Linux system. The backup process includes checking if Git is installed, committing the files to a Git repository, and pushing the changes to a remote repository. Additionally, the project includes a worker script that runs the backup daily at a specified time and retries in case of failure.

## Features

- Automated backup of user files.
- Git integration for version control.
- Daily scheduled backups.
- Error handling and retry mechanism.
- Detailed logging of backup operations.

## Requirements

- Python 3.12
- Flask
- Git
- Scheduler

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
2. **Create a Virtual Env**

   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt



4. **Licemse**

   
### Explanation:

- **Overview**: Provides a high-level summary of the project.
- **Features**: Lists the main features of the project.
- **Requirements**: Specifies the necessary tools and libraries.
- **Setup**: Instructions to set up the project, including cloning the repository, creating a virtual environment, installing dependencies, and configuring environment variables.
- **Usage**: Explains how to run the backup script and start the worker.
- **Example Scripts**: Includes the main parts of the backup and worker scripts.
- **Logging**: Information about where logs are stored and what they include.
- **Contributing**: Encourages contributions and provides guidance on how to contribute.
- **License**: Specifies the license for the project.


