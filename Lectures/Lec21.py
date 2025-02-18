def check_if_palindrome(string):
    if string == "":
        return True
    return string[0] == string[-1] and check_if_palindrome(string[1:-1])
def mystery(number):
    if number <= 1:
        return 1
    return 1 + mystery(number // 2)

def is_target_in_list(target, nested_list):
    if type(nested_list) == int:
        return nested_list == target
    for element in nested_list:
        if is_target_in_list(target, element):
            return True
    return False

def biggest_multiple_of_five(nested_list):
    if type(nested_list) == int:
        if nested_list % 5 == 0:
            return nested_list
        else:
            return None
    biggest = None
    for element in nested_list:
        best_from_element = biggest_multiple_of_five(element)
        if best_from_element is not None and \
                (biggest is None or best_from_element > biggest):
            biggest = best_from_element
    return biggest


def main():
    print(check_if_palindrome('deed'))
    print(mystery(40))
    print(is_target_in_list(6, [1, 2, [3, [4, 5]], 6]))
    print(biggest_multiple_of_five([3, 2, 1, [5, 10, 15, [50, 40, 60], 30], 65]))
if __name__ == "__main__":
    main()