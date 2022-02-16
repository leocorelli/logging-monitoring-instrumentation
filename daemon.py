from random import choices
from time import sleep

#LOGGING
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')

FRUIT = ["apple", "cherry", "strawberry"]
TIME = 2

while True:
    logger.info("Looping Daemon")
    logger.info(f"This is INFO fruit: {choices(FRUIT)}")
    logger.debug(f"This is DEBUG fruit: {choices(FRUIT)}")
    print(f"Sleeping for {TIME}")
    sleep(TIME)