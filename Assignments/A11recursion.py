"""
Initial code written by David Johnson, University of Utah.
This, and all derived works may not be publicly shared.

Assignment completed by David Peters
"""


def flatten_list(element):
    """
    Takes number(s) and makes a list of the number(s) with nesting removed
    :param element: an integer or a list of integers
    :return: a list of the numbers with nesting removed
    """

    if type(element) == int:  # Base case if element is a number
        return [element]

    flattened_list = []  # Create accumulation list
    for item in element:  # Loop through each part of the element
        flattened_list += flatten_list(item)  # Recursive adding of the element
    return flattened_list


def length_of_longest_string(element):
    """
    Finds the length of the longest string in a list or nested loop
    :param element: a string or a list of strings
    :return: length of the longest string
    """

    if type(element) == str:  # Base case is if element is just a string
        return len(element)  # Returns the length of the string

    longest = 0  # Create optimization variable
    for item in element:  # Loop over each item in element
        length = length_of_longest_string(item)  # Recursive function to find length of each string
        if length > longest:  # If it's longer then longest then make it longest
            longest = length
    return longest


def main():
    print("Testing flatten_list([[2], 4, 3, 2, [5, [3, 2], 5], [7, 8]])), expecting [2, 4, 3, 2, 5, 3, 2, 5, 7, 8]",
          "and got:", flatten_list([[2], 4, 3, 2, [5, [3, 2], 5], [7, 8]]))
    print("Testing flatten_list(3), expecting [3], and got:", flatten_list(3))
    print("Testing flatten_list([1, [2, [3]]), expecting [1, 2, 3], and got:", flatten_list([1, [2, [3]]]))
    print("Testing length_of_longest_string('samuel', 'bob', ['joe', 'david']]), expecting 6 and got:",
          length_of_longest_string(["samuel", "bob", ["joe", "david"]]))
    print("Testing length_of_longest_string(['Titanic', 'Boat', 'Ocean', 'School', 'stuff']), expecting 7 and got:",
          length_of_longest_string(['Titanic', 'Boat', 'Ocean', 'School', 'stuff']))
    print("Testing length_of_longest_strint([]), expecting 0 and got:", length_of_longest_string([]))


if __name__ == "__main__":
    main()
