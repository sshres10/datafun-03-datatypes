"""
Task 3. Numeric Lists

"""

import math
import statistics
import logging
from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)

numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def calculate_average_goals(total_goals, total_games):
    """
    Calculate the average goals per game for a soccer team.

    total_goals: Total number of goals scored by the team.
    total_games: Total number of games played by the team.

    return: The average goals per game (rounded to the nearest integer).
    """
    if total_games == 0:
        return 0
    
    average = total_goals / total_games
    return round(average)

average_goals = calculate_average_goals(10, 5)
logger.info(f"Average goals per game: {average_goals}")

# Create list1 - a fairly long (20 or more list of numbers)
list1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

# Create listx representing 10 integer times
listx = list(range(10))

# Create listy representing 10 values/measurements read at those times
listy = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1]

# Create listy so the values are pretty much linear but not exactly - we'll draw a straight-line through the data to make predictions.

# List Statistics
mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)
stdev = round(statistics.stdev(listy))
variance = round(statistics.variance(listy))

logger.info(f"Mean: {mean}")
logger.info(f"Median: {median}")
logger.info(f"Mode: {mode}")
logger.info(f"Standard Deviation: {stdev}")
logger.info(f"Variance: {variance}")


logger, logname = setup_logger(__file__)


# Calculate the correlation between listx and listy
correlation = statistics.correlation(listx, listy)

# Calculate the slope and intercept of the best fit line
slope, intercept = statistics.linear_regression(listx, listy)

# Set a future time to 15
future_time = 15

# Predict the y value at the future time y = mx + b where m is the slope and b is the y intercept
predicted_y = slope * future_time + intercept

logger.info(f"Correlation between x and y: {correlation}")
logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")
logger.info(f"Predicted y value at future time {future_time}: {predicted_y}")

# Create a list of numbers
numbers = list1

# Calculate the minimum value in the list
minimum = min(numbers)

# Calculate the maximum value in the list
maximum = max(numbers)

# Calculate the length of the list
length = len(numbers)

# Calculate the sum of all values in the list
total = sum(numbers)

# Calculate the average of all values in the list using two values already calculated
average = total / length

# Create a set from the list
unique_numbers = set(numbers)

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Sort the list in descending order
reverse_sorted_numbers = sorted(numbers, reverse=True)

logger.info(f"Minimum value: {minimum}")
logger.info(f"Maximum value: {maximum}")
logger.info(f"Length of list: {length}")
logger.info(f"Sum of all values: {total}")
logger.info(f"Average of all values: {average}")
logger.info(f"Unique numbers: {unique_numbers}")
logger.info(f"Sorted numbers: {sorted_numbers}")
logger.info(f"Reverse sorted numbers: {reverse_sorted_numbers}")

# Create a new list
lst = [1, 2, 3, 4, 5]

# Append a single value to the list
lst.append(6)

# Extend the list with a new list you pass in
lst.extend([7, 8, 9])

# Insert a value at an index
lst.insert(0, 0)

# Remove a value from the list
lst.remove(5)

# Count how many times a value appears in the list
count = lst.count(2)

# Sort the list in ascending order
lst.sort()

# Sort the list in descending order
lst.sort(reverse=True)

# Create a copy of the list
lst_copy = lst.copy()

# Pop the first item off the top of the list/stack
first_item = lst.pop(0)

# Pop the last item off the bottom of the list/stack
last_item = lst.pop()

logger.info(f"Minimum value: {min(lst)}")
logger.info(f"Maximum value: {max(lst)}")
logger.info(f"Length of list: {len(lst)}")
logger.info(f"Sum of all values: {sum(lst)}")
logger.info(f"Average of all values: {(sum(lst) / len(lst))}")
logger.info(f"Unique numbers: {set(lst)}")
logger.info(f"Sorted numbers: {sorted(lst)}")
logger.info(f"Reverse sorted numbers: {sorted(lst, reverse=True)}")

# Create a list of numbers
numbers = [10, 11, 12, 13, 14, 15]

# Use filter() to keep only the numbers less than 4
filtered_numbers = list(filter(lambda x: x < 4, numbers))
logger.info(f"Filtered numbers: {filtered_numbers}")

# Use filter() to keep only the even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
logger.info(f"Even numbers: {even_numbers}")

# Use map() to calculate the cube root of each number
cubed_numbers = list(map(lambda x: math.pow(x, 1/3), numbers))
logger.info(f"Cubed numbers: {cubed_numbers}")

# Use map() to calculate the volume of a cube with a side equal to each number
volumes = list(map(lambda x: math.pow(x, 3), numbers))
logger.info(f"Volumes: {volumes}")

# Use list comprehension to filter the numbers less than 4
filtered_numbers = [x for x in list1 if x < 4]
logger.info(f"Filtered numbers: {filtered_numbers}")

# Use list comprehension to triple each value in the list
tripled_numbers = [x * 3 for x in list1]
logger.info(f"Tripled numbers: {tripled_numbers}")

# Use list comprehension to transform the numeric list into another numeric list using a transformation of your choice
transformed_numbers = [math.pow(x, 2) + 1 for x in list1]
logger.info(f"Transformed numbers: {transformed_numbers}")
