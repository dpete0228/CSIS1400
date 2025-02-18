# Assignment 8 - Search Optimization for CS1400
# Created by ooooooohhh secret.

from timeit import default_timer
import random

# Finds the biggest number, shifts it up to 100, then shifts the rest up by same amount
def curve_scores(integer_list):
    biggest_so_far = None
    curved_list = []
    if integer_list == []:
        return integer_list
    for integer in integer_list:    # First, find the biggest integer
        if biggest_so_far == None or integer > biggest_so_far:
            biggest_so_far = integer
    curve_amount = 100 - biggest_so_far  # Make curved list
    for integer in integer_list:
        curved_list.append(integer + curve_amount)
    return curved_list


# Finds an item in list, and compares item to the rest of the list. Repeat. True if there are duplicates, False if none.
def contains_duplicate(list_of_strings):
    for chosen_index in range(len(list_of_strings)):
        for checking_index in range(chosen_index + 1, len(list_of_strings)):
            # print("chosen index:",chosen_index, "comparing to:",checking_index)
            if list_of_strings[chosen_index] == list_of_strings[checking_index]:
                return True
    return False


# Convert list of ints into a single string of those integers. ie: "[1, 2, 3]"
def list_to_string(list):
    # watch out for last value, make it work w/ empty list
    new_string = "["
    for integer_index in range(len(list)):
        new_string += str(list[integer_index])
        if integer_index != len(list) - 1:
            new_string += ", "
    new_string += "]"
    return new_string

# Return the integer (greater than 0) that's the smallest multiple of 3, or None if there isn't any
def find_smallest_positive_multiple_of_three(integer_list):
    smallest_int = None
    for integer in integer_list:
        if integer % 3 == 0 and integer > 0 and (smallest_int == None or integer < smallest_int):
            smallest_int = integer
    return smallest_int

# --------------------- Part 2 of assignment --------------------------------


# Searches a list of integers for a target integer. Returns true if target is in list. False if it's not.
def sequential_search(target_integer, ordered_list):
    """
    Searches for a target by comparing to every item in the whole list

    :param target_integer: The integer to search for
    :param ordered_list: Input list of ordered integers
    :return: True if item is in list, False if it's not
    """
    for integer in ordered_list:
        if integer == target_integer:
            return True
    return False


# Searches for target int in ordered list using higher or lower middle values. True if in list, False otherwise
def binary_search(target, ordered_list):  # Note: list MUST be in order least to greatest
    """
    Searches by halving the list, checking value, then going higher or lower if < or > than value, repeats until found.

    :param target: Integer to search for
    :param ordered_list: Input list of values to search in. MUST be ordered.
    :return:
    """
    start_index = 0
    stop_index = len(ordered_list) - 1
    while start_index <= stop_index:
        middle_index = (start_index + stop_index) // 2  # halve the list
        if ordered_list[middle_index] == target:
            return True
        elif ordered_list[middle_index] < target:
            start_index = middle_index + 1
        else:
            stop_index = middle_index - 1
    # Code gets here if target us not in list
    return False

# Make values in a dictionary smaller decimals
def clean_up_long_values(dictionary):
    for key in dictionary:
        dictionary[key] = f'{dictionary[key]:.8f}'
    return dictionary


# times how long a process takes to compute, prints the result.
def measure_search_times():
    list_size = 10000
    average_seq_search_times = {}
    average_binary_search_times = {}

    while list_size < 10000001:
        # Initialize variables
        big_list2 = list(range(list_size))
        randoms_from_list = []

        start = default_timer()  # start timer for SEQUENTIAL SEARCH

        for count in range(10):        # Grab random numbers from the list
            randoms_from_list.append(random.randint(0,list_size))
        for selection in randoms_from_list:        # Sequential search those randoms
            sequential_search(selection, big_list2)

        stop = default_timer()  # stop timer for SEQUENTIAL SEARCH
        average_seq_search_times[list_size] = ((stop - start) / 10)

        # -------------------- organization breaker - stop and refresh
        randoms_from_list = []

        # -------------------- organization breaker - begin binary search test

        start = default_timer()  # start timer for BINARY SEARCH

        for count in range(10):        # Grab random numbers from the list
            randoms_from_list.append(random.randint(0,list_size))
        for selection in randoms_from_list:        # Sequential search those randoms
            binary_search(selection, big_list2)

        stop = default_timer()  # stop timer for BINARY SEARCH
        average_binary_search_times[list_size] = ((stop - start) / 10)

        # Start again for big_list * 10
        list_size = list_size * 10
    # End the searches while loop ----------------------------------------
    # clean up values:
    average_seq_search_times = clean_up_long_values(average_seq_search_times)
    average_binary_search_times = clean_up_long_values(average_binary_search_times)

    # Report values
    reporting_size2 = 10000
    while reporting_size2 < 10000001:
        print("For a list size of:", reporting_size2)
        print("     Average sequential search time was:", average_seq_search_times[reporting_size2])
        print("     Average binary search time was:", average_binary_search_times[reporting_size2])
        reporting_size2 = reporting_size2 * 10

    # Part 7 - shuffle time
    list_size2 = 10000
    while list_size2 < 10000001:
        # Initialize variables
        big_list2 = list(range(list_size2))
        random.shuffle(big_list2)
        randoms_from_list = []

        start = default_timer()  # start timer for SEQUENTIAL SEARCH

        for count in range(50):        # Grab random numbers from the list
            randoms_from_list.append(random.randint(0,list_size2))
        for selection in randoms_from_list:        # Sequential search those randoms
            sequential_search(selection, big_list2)

        stop = default_timer()  # stop timer for SEQUENTIAL SEARCH
        average_seq_search_times[list_size2] = ((stop - start) / 50)

        # -------------------- organization breaker - stop and refresh
        randoms_from_list = []
        # -------------------- organization breaker - begin binary search test

        start = default_timer()  # start timer for BINARY SEARCH
        big_list2.sort()
        for count in range(50):        # Grab random numbers from the list
            randoms_from_list.append(random.randint(0,list_size2))
        for selection in randoms_from_list:        # Sequential search those randoms
            binary_search(selection, big_list2)

        stop = default_timer()  # stop timer for BINARY SEARCH
        average_binary_search_times[list_size2] = ((stop - start) / 50)

        # Start again for big_list * 10
        list_size2 = list_size2 * 10
    # End the searches while loop ----------------------------------------
    # clean up values:
    average_seq_search_times = clean_up_long_values(average_seq_search_times)
    average_binary_search_times = clean_up_long_values(average_binary_search_times)

    # Report values
    reporting_size2 = 10000
    print()  # make it readable
    print("----------------------------------------------------------------------")
    print("Shuffled the list, did it 50 times instead of 10")
    print("Binary list uses .sort() in order to work.")
    while reporting_size2 < 10000001:
        print("For a list size of:", reporting_size2)
        print("     Average sequential search time was:", average_seq_search_times[reporting_size2])
        print("     Average binary search time was:", average_binary_search_times[reporting_size2])
        reporting_size2 = reporting_size2 * 10








# ---------------- def main / begin tests --------------------------
def main():
    pass
    # Note to self: run lots of tests! MAKE THEM SAY WHAT ANSWER IS EXPECTED, AND WHAT'S INPUTTED
    print("Testing curve_scores function")
    print("test1: inputting [45, 85, 90], expecting [55, 95, 100]. Got:", curve_scores([45, 85, 90]))
    print("test2: inputting [100, 20, 30, 0, 95], expecting [100, 20, 30, 0, 95]. Got:", curve_scores([100, 20, 30, 0, 95]))
    print("test3: inputting [], expecting []. Got:", curve_scores([]))
    print()
    print("Testing contains_duplicate function")
    print("test1:", "inputting ['hi', 'no', 'a', 'b', 'c', 'd'], expecting False, got:", contains_duplicate(["hi", "no", "a", "b", "c", "d"]))
    print("test2:", 'inputting ["hi", "no", "a", "b", "c", "c"]' , "expecting True, got:", contains_duplicate(["hi", "no", "a", "b", "c", "c"]))
    print("test3:", 'inputting ["hi", "c", "a", "b", "c", "c"]',"expecting True, got:", contains_duplicate(["hi", "c", "a", "b", "c", "c"]))
    print("test4:", 'inputting ["boy", "C", "a", "b", "c", "boy"]', "expecting True, got:", contains_duplicate(["boy", "C", "a", "b", "c", "boy"]))
    print("test5:", 'inputting ["hi", "C", "a", "b", "c", "bye"]', "expecting False, got:", contains_duplicate(["hi", "C", "a", "b", "c", "bye"]))
    print("test6:", 'inputting ["fly", "rock", "flip", "abc"]', "expecting False, got:", contains_duplicate(["fly", "rock", "flip", "abc"]))
    print("test7:", 'inputting []', "expecting False, got:", contains_duplicate([]))
    print()
    print("Testing list_to_string function")
    print("test1:", 'inputting [1, 2, 3, 4, 5, 6, 7]', "expecting [1, 2, 3, 4, 5, 6, 7], and got:", list_to_string([1, 2, 3, 4, 5, 6, 7]))
    print("test2:", 'inputting [890, 0, 1234, "string", -3, ]', "expecting [890, 0, 1234, 'string', -3, ], and got:", list_to_string([890, 0, 1234, "string", -3, ]))
    print("test3:", 'inputting []', "expecting [], and got:" , list_to_string([]))
    print()
    print("Testing find_smallest_positive_multiple_of_three function")
    print("test1:", 'inputting [-3, 0, 2, 3, 1, 6]', "expecting 3, and got:", find_smallest_positive_multiple_of_three([-3, 0, 2, 3, 1, 6]))
    print("test2:", 'inputting [0,9,2,30,3]', "expecting 3, and got:", find_smallest_positive_multiple_of_three([0,9,2,30,3]))
    print("test3:", 'inputting [2, 4, 7, 10, -3]', "expecting None, and got:", find_smallest_positive_multiple_of_three([2, 4, 7, 10, -3]))
    print("test3:", 'inputting [50, 60, 80, 9, 1]', "expecting 9, and got:", find_smallest_positive_multiple_of_three([50, 60, 80, 9, 1]))
    print()
    print("Testing Binary_search function")
    print("test1:", "expecting True, got:", binary_search(8,[1,2,3,4,5,5,6,7,8,9,10]))
    print("test2:", "expecting True, got:",binary_search(-5,[-30,-24,-5,-2,9,100,2000,90000]))
    print("test3:", "expecting False, got:",binary_search(100,[-9,100,8,7,69]))
    print("test4:", "expecting False, got:",binary_search(100,[1,3,6,8,10]))
    print()
    print("Measure search times function tests")

    measure_search_times()

    print()
    print("(why was this assignment so long????)")

# Data from original search
#
# Measure search times function tests
# For a list size of: 10000
#      Average sequential search time was: 0.00008281
#      Average binary search time was: 0.00000225
# For a list size of: 100000
#      Average sequential search time was: 0.00067712
#      Average binary search time was: 0.00000351
# For a list size of: 1000000
#      Average sequential search time was: 0.00862613
#      Average binary search time was: 0.00000622
# For a list size of: 10000000
#      Average sequential search time was: 0.10991458
#      Average binary search time was: 0.00000738
#
# Report from original search:
#
# The sequential search time grows exponentially when the list size is raised by x10.
# Binary searches are remarkably faster, especially with greater list sizes. As the list size multiplies by 10,
# the binary search time increases by about a 1/100,000 of a second. If we search in huge lists, sequential
# searches take extremely long times. Meanwhile, it doesn't add much time at all for binary searches.
# When the list size is small, the two methods are more equal in timing.
# In fact, a sequential search may be faster if the first value checked is the correct target value.
#
# ---------------------------------------------------------
#
# Shuffled the list, did it 50 times instead of 10
# Binary list uses .sort() in order to work.
#
# For a list size of: 10000
#      Average sequential search time was: 0.00011525
#      Average binary search time was: 0.00002320
# For a list size of: 100000
#      Average sequential search time was: 0.00137525
#      Average binary search time was: 0.00029355
# For a list size of: 1000000
#      Average sequential search time was: 0.04193222
#      Average binary search time was: 0.00564129
# For a list size of: 10000000
#      Average sequential search time was: 0.57389352
#      Average binary search time was: 0.07126874
#
# Report:
# Binary search starts off being more efficient than sequential with this method, but at larger lists, that changes.
# With the list being shuffled, the binary method has to sort in order to work. Sorting large lists adds a lot of time.
# So with these larger lists, binary eventually becomes less efficient because of this sorting.
#
# Overall, binary is an efficient way of searching large lists, especially compared to sequential searches.
# Binary searches handle large lists easily as long as they're sorted.
# If the list is either randomized and/or small, then a sequential search may be better.
# However, the two methods will have similar computation times if the list is small.
#


if __name__ == "__main__":
    main()
