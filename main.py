import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger_file_handler = logging.FileHandler('weather.log', encoding="utf8")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    logger.info("API KEY NOT AVAILABLE")

if __name__ == "__main__":
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Kraków&appid={API_KEY}&units=metric")
    if r.status_code == 200:
        data = r.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        logger.info(f"Weather in Cracow: {temperature} celsius, status: {description} ")
