import logging


logging.basicConfig(level=logging.DEBUG)

log_filename = "logs/app.log"
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
