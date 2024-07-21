import datetime
import logging
import os
import subprocess

# Change current user
USER_HOME = "/home/devops"

# Change for your GitHub repository path
GIT_REPO_PATH = "/path/to/your/repository"
GIT_COMMIT_MESSAGE = f"Backup {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
LOG_FILE = "/path/to/your/logfile.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def run_command(command):
    """Executes a shell command and returns the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Error executing command: {command}\nOutput: {result.stdout}\nError: {result.stderr}")
        return None
    return result.stdout

def backup_files():
    """Performs backup of the devops user files."""
    logging.info("Starting backup process.")
    start_time = datetime.datetime.now()
    
    os.chdir(USER_HOME)
    
    # Initialize the Git repository if it is not already initialized
    if not os.path.exists(os.path.join(GIT_REPO_PATH, ".git")):
        run_command(f"git init {GIT_REPO_PATH}")
    
    os.chdir(GIT_REPO_PATH)
    
    # Add all files and folders to the Git repository
    run_command("git add .")
    
    # Commit the changes with the backup message
    run_command(f'git commit -m "{GIT_COMMIT_MESSAGE}"')
    
    # Push the changes to the remote repository
    run_command("git push origin main")
    
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    logging.info(f"Backup completed successfully in {duration} seconds.")

if __name__ == "__main__":
    backup_files()
