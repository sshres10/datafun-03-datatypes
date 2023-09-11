import doctest
from util_datafun_logger import setup_logger

# Set up logging
logger, logname = setup_logger(__file__)

def compare_two_plays():
    ''' This function compares two plays by Shakespeare.'''
    logger.info("Calling compare_two_plays()")
        
    # read from file and get a list of words
    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    logger.info(f"List of words from play 1: {wordlist1}")

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  # split on whitespace

    logger.info(f"List of words from play 2: {wordlist2}")

    # Remove duplicates by creating two sorted sets
    wordset1 = sorted(set(wordlist1))
    wordset2 = sorted(set(wordlist2))

    # initialize a variable maxlen = 10
    maxlen = 10

    # use a list comprehension to get a list of words longer than 10
    longwordset1 = set([word for word in wordset1 if len(word) > maxlen])
    longwordset2 = set([word for word in wordset2 if len(word) > maxlen])

    # find the intersection of the two sets
    longwords = longwordset1 & longwordset2

    # print the length of the sets and the list
    print(len(longwordset1))
    print(len(longwordset2))
    print(len(longwords))
    print()
    print(f"{sorted(longwords) = }")
    print()

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    compare_two_plays()

    logger.info("Complete the code to compare two plays.")
    show_log()
