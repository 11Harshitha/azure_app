import logging

# Configure logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app_log/app.log"),
        # logging.StreamHandler()
    ]
)

# Create logger instance
logger = logging.getLogger("MyAppLogger")
