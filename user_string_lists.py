"""
Purpose: Illustrate string lists for Soccer 

"""
import random
import logging

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Define shared data ..........................................
import random

def process_text_soccer():
    """Read in text_soccer.txt and process it"""
    logger.info("Calling process_text_soccer()")


# Define your lists
listA = ["goalkeeper", "defender", "midfielder", "forward"]
listB = ["penalty kick", "corner kick", "free kick", "throw-in"]
listC = ["yellow card", "red card", "offside", "foul"]
listD = ["Premier League", "La Liga", "Serie A", "League One"]
listE = ["World Cup", "Euro", "Asia Cup", "Copa America"]

# String Lists 1: Using Python Built-in Functions
tupleAB = list(zip(listA, listB))
tupleCD = list(zip(listC, listD))
logging.info(f"Tuple AB: {tupleAB}")
logging.info(f"Tuple CD: {tupleCD}")

# String Lists 2: Random Choice
random_item = random.choice(listE)
logging.info(f"A random item from listE is {random_item}.")

# String Lists 3: Get Unique Words
def process_text_soccer():
    """Read in text_soccer.txt and process it"""
    logger.info("Calling process_text_soccer()")

    # read in soccer to get a list of words
    with open("text_soccer.txt", "r") as fileObject:
        text = fileObject.read()
        words = text.split()  # split on whitespace
        unique_words = sorted(set(words))  # remove duplicates by making a set
        logging.info(f"There are {len(unique_words)} unique words in soccer.txt.")
                              
                              