"""
Purpose: Illustrate tuples, sets, and dictionaries for Soccer in Python.


"""
# Import the logger
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def illustrate_soccer_tuples():
    """This function illustrates tuples in Python using a soccer as a domain."""

    # Create some tuples
    teamA = ('Saka', 'Martinelli', 'Gabriel')
    teamB = ('Saliba', 'Zinchenko', 'Tomiyasu')

    logger.info(f"{teamA = }")
    logger.info(f"{teamB = }")

    # tuple concatenation
    allPlayers = teamA + teamB

    # tuple repetition
    teamAThrice = teamA * 3

    logger.info(f"{allPlayers = }")
    logger.info(f"{teamAThrice = }")

    # tuple membership testing
    hasSaka = 'Saka' in teamA  # True
    hasSaliba = 'Saliba' in teamA  # False

    logger.info(f"Does teamA have Saka? {hasSaka}")
    logger.info(f"Does teamA have Saliba? {hasSaliba}")

    # tuple indexing (0 is first, -1 is last, or 1 less than the length)
    firstPlayer = teamA[0]
    secondPlayer = teamA[1]
    lastPlayer = teamA[-1]

    logger.info(f"First player in Team A: {firstPlayer}")
    logger.info(f"Second player in Team A: {secondPlayer}")
    logger.info(f"Last player in Team A: {lastPlayer}")

illustrate_soccer_tuples()


"""This function illustrates Soccer sets in Python."""

# Import the logger
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def illustrate_soccer_sets():
    """This function illustrates sets in Python using a soccer as a domain."""

    # Create some sets
    teamA = {'Messi', 'Neymar', 'Mbappe'}
    teamB = {'Ronaldo', 'Ronaldinho', 'Zlatan'}

    logger.info(f"{teamA = }")
    logger.info(f"{teamB = }")

    # set union
    allPlayers = teamA | teamB

    # set intersection
    commonPlayers = teamA & teamB

    # set difference
    uniquePlayersA = teamA - teamB

    logger.info(f"{allPlayers = }")
    logger.info(f"{commonPlayers = }")
    logger.info(f"{uniquePlayersA = }")

    # sets are often used to remove duplicates from a list
    playersList = ['Messi', 'Neymar', 'Messi', 'Mbappe', 'Neymar', 'Mbappe']
    uniquePlayersList = list(set(playersList))

    logger.info(f"Original list: {playersList}")
    logger.info(f"List after removing duplicates: {uniquePlayersList}")

illustrate_soccer_sets()

"""This function illustrates Soccer dictionaries in Python."""

def illustrate_soccer_dictionaries():
    """This function illustrates dictionaries in Python using a soccer as a domain."""

    # Create some dictionaries
    playerA_dict = {"name": "Messi", "age": 34, "team": "Inter Miami"}
    playerB_dict = {"name": "Ronaldo", "age": 36, "team": "Al Nassr"}

    logger.info(f"{playerA_dict = }")
    logger.info(f"{playerB_dict = }")

    # Create a dictionary of player ratings
    player_ratings_dict = {"Messi": 98, "Ronaldo": 92, "Neymar": 85}
    logger.info(f"{player_ratings_dict = }")

    # Create a dictionary of team data
    team_data_dict = {
        "team": ["PSG", "Inter Miami", "Al Nassr", "Real Madrid"],
        "league": ["Ligue 1", "MLS", "Saudi League", "La Liga"],
        "points": [89, 85, 86, 88],
    }
    logger.info(f"{team_data_dict = }")

    # Dictionaries can be used to store and aggregate statistical data,
    # such as counts or sums. For example, a dictionary of goal-count pairs.

    goal_list = ['Messi', 'Ronaldo', 'Messi', 'Neymar', 'Messi', 'Ronaldo']

    goal_counts_dict = {}
    for player in goal_list:
        if player in goal_counts_dict:
            goal_counts_dict[player] += 1
        else:
            goal_counts_dict[player] = 1

    logger.info("Goal count is a good way to analyze player performance.")
    logger.info(f"Given goal_list, the goal_counts_dict = {goal_counts_dict}")

illustrate_soccer_dictionaries()
