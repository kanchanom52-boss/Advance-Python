import logging

def setup_logger():
    """Configures logging to record to both a file and the console."""
    # 1. Create a root logger instance
    logger = logging.getLogger("MultiPurposeLogger")
    logger.setLevel(logging.DEBUG)  # Capture everything from DEBUG up

    # 2. Define a clean format pattern
    log_format = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 3. File Handler: Logs WARNING and above into a file
    file_handler = logging.FileHandler("app_log.txt", mode="w")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(log_format)

    # 4. Console Handler: Logs all activities (DEBUG and above) directly to screen
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(log_format)

    # 5. Attach handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

if __name__ == "__main__":
    log = setup_logger()
    
    # Demonstrate all standard logging severity levels
    log.debug("Diagnostic data gathered. This is only visible on the console.")
    log.info("System initialized successfully.")
    log.warning("Low disk space detected! (This message is also saved to app_log.txt)")
    log.error("Failed to connect to the database pipeline.")
    
    # Demonstrate logging unexpected errors using exceptions
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        log.critical("System crash avoided! Exception details captured below:", exc_info=True)
