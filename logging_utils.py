
# utils/logging_utils.py
# This file contains utility functions for logging.
import logging

def setup_logging():
    logging.basicConfig(filename='chatbot_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
