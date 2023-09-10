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

# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.


def process_text_soccer():
    """Read in text_soccer.txt and process it"""
    logger.info("Calling process_text_soccer()")

    try:
        # read in soccer to get a list of words
        with open("text_soccer.txt", "r") as fileObject:
            text = fileObject.read()
            words = text.split()  # split on whitespace
            unique_words = sorted(set(words))  # remove duplicates by making a set
            logging.info(f"There are {len(unique_words)} unique words in soccer.txt.")
    except FileNotFoundError:
        logging.error("File not found: text_soccer.txt")

def foul():
    """Which foul is it?"""
    logger.info("Calling foul()")

    foul_committed = True  # TODO: change this when ready
    logger.info(f"foul_committed = {foul_committed}")

    if not foul_committed:
        logger.info("No foul committed yet")
        logger.info("Existing the function early without further processing.")
        return

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    process_text_soccer()
    show_log()
  
        
    
                              
                              