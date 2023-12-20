# utils/maintenance_utils.py
import os
import shutil
import schedule
from datetime import datetime

def cleanup_logs(log_directory, retention_period_days=30):
    """
    Clean up old log files to manage disk space.

    Parameters:
    - log_directory (str): Path to the directory containing log files.
    - retention_period_days (int): Number of days to retain log files.
    """
    try:
        current_time = datetime.now()
        for log_file in os.listdir(log_directory):
            log_file_path = os.path.join(log_directory, log_file)
            file_creation_time = datetime.fromtimestamp(os.path.getctime(log_file_path))
            age_in_days = (current_time - file_creation_time).days

            if age_in_days > retention_period_days:
                os.remove(log_file_path)
                print(f"Deleted old log file: {log_file_path}")

    except Exception as e:
        print(f"Error during log cleanup: {e}")

def update_models(classifier_model, code_generation_model, new_data):
    """
    Update machine learning models based on new data.

    Parameters:
    - classifier_model: Instance of the classifier model.
    - code_generation_model: Instance of the code generation model.
    - new_data (list): List of examples containing new data.
    """
    try:
        # Update classifier model
        classifier_model.update_model(new_data)

        # Update code generation model
        code_generation_model.update_model(new_data)

        print("Models updated successfully.")

    except Exception as e:
        print(f"Error updating models: {e}")

def perform_regular_maintenance():
    """
    Schedule regular maintenance tasks.
    """
    # Example: Clean up logs every Sunday at 3 AM
    schedule.every().sunday.at("03:00").do(cleanup_logs, log_directory="logs/")

    # Example: Update models every month
    schedule.every().month.at("02:00").do(update_models, classifier_model, code_generation_model, new_data)

    # Add more maintenance tasks as needed

    while True:
        schedule.run_pending()

