import datetime
import logging
from sched import scheduler
import subprocess

# Logger configuration
LOG_FILE = "/path/to/your/logfile.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def run_backup():
    """Executes the backup script."""
    try:
        start_time = datetime.datetime.now()
        subprocess.run(["python3.12", "scripts/backup_script.py"], check=True)
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).total_seconds()
        logging.info(f"Backup successfully completed in {duration} seconds.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Backup failed: {e}. Reprocessing...")
        run_backup()

# Schedule the backup daily at :00 Brasília time
scheduler.every().day.at(":00").do(run_backup)

logging.info("Worker started. Waiting for backup execution time...")

while True:
    scheduler.run_pending()
    datetime.time.sleep(60)  # Waits one minute before checking again
