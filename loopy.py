from random import choices
from time import sleep

# LOGGING
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("simpleExample")

FRUIT = ["apple", "cherry", "strawberry"]
TIME = 2

while True:
    logging.info("Looping Daemon")
    logging.info(f"This is INFO fruit: {choices(FRUIT)}")
    logging.debug(f"This is DEBUG fruit: {choices(FRUIT)}")
    print(f"Sleeping for {TIME}")
<<<<<<< HEAD:daemon.py
    sleep(TIME)
=======
    sleep(TIME)
>>>>>>> 78476cf9b7aa69c3f937a24f991f5e6477875f0b:loopy.py
