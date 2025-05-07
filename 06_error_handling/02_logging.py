import logging

try:
    pass # Your potentially error-prone code here
    
except Exception as e:
    logging.error(f"An error occurred: {e}")  # Logs the exception with details