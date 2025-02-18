def binary_search(my_list, target_value):
    start_index = 0
    stop_index = len(my_list) - 1

    # Repeat until start_index and stop_index switch places:
    while start_index <= stop_index:
        # Calculate the middle_index
        middle_index = (start_index + stop_index) // 2
        # If the value at middle_index is your target value, found it!
        if my_list[middle_index] == target_value:
            return middle_index
        # If the value at middle_index is LESS THAN your target value,
            # set start_index to middle_index + 1
        elif my_list[middle_index] < target_value:
            start_index = middle_index + 1
        # If the value at middle_index is GREATER THAN your target value,
            # set stop_index to middle_index - 1
        else:
            stop_index = middle_index - 1

    return None

def main():
    number_list = [1, 5, 9, 13, 15, 19, 21, 30]
    animals = ['cat', 'dog', 'fish', 'shark', 'zebra']
    #print(binary_search(number_list,15))
    print(binary_search(animals,'dog'))

if __name__=="__main__":
    main()