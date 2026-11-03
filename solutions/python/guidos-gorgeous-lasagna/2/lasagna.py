"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_left_to_bake = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_left_to_bake


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time .

    Parameters:
        number_of_layers (int): The number of layers the lasagna has.

    Returns:
        int: The total prep time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers of lasagna and calculates the total prep time assuming each layer prep time is 'PREPARATION_TIME'.
    """
    totalpreptime = number_of_layers * PREPARATION_TIME
    return totalpreptime

#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers,elapsed_time_in_minutes):
    """Calculate the total elapsed time spent in the kitchen .

    Parameters:
        number_of_layers (int): The number of layers the lasagna has.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed time (in minutes) derived from 'PREPARATION_TIME' per layer of lasagna and the elapsed bake time.

    Function that takes the number of layers of lasagna, 'PREPARATION_TIME' per layer, and elapsed_baking_time to calculate the     total_elapsed_time (in minutes).
    """
    total_elapsed_time = PREPARATION_TIME * number_of_layers + elapsed_time_in_minutes
    return total_elapsed_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
