import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def retry_request(func, retries=3, delay=2):

    for i in range(retries):

        try:
            return func()

        except Exception as e:

            logging.warning(f"Retry {i+1}/{retries} failed")

            time.sleep(delay)

    logging.error("Max retries exceeded")

    return None