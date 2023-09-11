# My Project 3

**Name:** Sushanta Shrestha
**Date:** September 10, 2023
**Domain:** Sports Analytics (Soccer)

# Import the logger
from util_datafun_logger import setup_logger

# Set up logging
logger, logname = setup_logger(__file__)

def soccer_players():
    """This function manages a list of soccer players."""
    logger.info("Calling soccer_players()")

    # List of soccer players
    players_attack = ["Saka", "Trossard", "Martinelli", "Viera"]

    # Add a forward
    players_attack.append("Henry")

    # Sort the list
    players_attack.sort()

    # Log the list of players
    logger.info(f"List of players: {players_attack}")

    # Return the list
    return players_attack

if __name__ == "__main__":
    # Call the function and log the result
    result = soccer_players()
    logger.info(f"Result: {result}")

    # At the end, read from the log file and display the information in the console
    with open(logname, 'r') as f:
        for line in f:
            print(line.strip())



