import random


# Functions to process audio samples.
# For CS 1400, written by David E. Johnson.
# Functions implementations by David Peters
# make_reversed_samples function takes a list and puts the numbers in reverse order
def make_reversed_samples(list_numbers):
    reversed_list = []  # make a reversed list variable
    for index in range(1, len(list_numbers) + 1):  # since starting at 1, have to do len + 1
        reversed_list.append(list_numbers[-index])  # adds the -index to the reversed list
    return reversed_list  # return the reversed list


# the make_louder_samples function takes a list of numbers and multiplies it by a scale parameter
def make_louder_samples(list_numbers, scale_number):
    louder_list = []  # make a louder list variable
    for number in list_numbers:  # looking at the stored number instead of the indices
        louder_list.append(number * scale_number)  # appends the scaled number to the louder list
    return louder_list  # returns the louder list


# the make_clipped_samples functions takes a list of numbers and sets all numbers above the +clip level
# to the +clip level and below the -clip level to the -clip level
def make_clipped_samples(list_numbers, clip_level):
    clipped_list = []  # make a clipped list variable
    for number in list_numbers:  # looping over the values instead of indices
        if number > clip_level:  # checking if it's above the +clip_level
            clipped_list.append(clip_level)  # if it is above, appending the clip_level
        elif number < -clip_level:  # checking if it's below the - clip level
            clipped_list.append(-clip_level)  # if it is below, appending the -clip_level
        else:
            clipped_list.append(number)  # if its the same or within the clip level appending the number
    return clipped_list  # returning the clipped list


# the make_noisy_samples function takes the list of numbers
# and adds or subtracts a random amount within the + or - noise level
def make_noisy_samples(list_numbers, noise_level):
    noisy_list = []  # make a noisy_list variable
    for number in list_numbers:  # looping over the values not the indices
        random_noise = random.randint(-noise_level, noise_level)  # chooses a random number between the + and
        # - noise_level
        noisy_list.append(random_noise + number)  # appending the added value and random noise to the noisy_list
    return noisy_list  # return the finished noisy_list


# the make_smoothed_samples function takes the average of the numbers before and after each number
def make_smoothed_samples(list_numbers):
    smoothed_list = []  # make a new smoothed_list variable
    for index in range(len(list_numbers)):  # looping over the indices of the list
        averaged_number = 0  # creating the averaged_number variable
        if index == 0:  # if it's the first index, only looking at the first and next index
            averaged_number = (list_numbers[index] + list_numbers[index + 1]) // 2  # setting the averaged_number
        elif index == len(list_numbers) - 1:  # if it's the last index, only looking at the last and the one before
            averaged_number = (list_numbers[index] + list_numbers[index - 1]) // 2  # setting the averaged_number
        else:  # if it's not the first/last then looking at the index both before and after
            averaged_number = (list_numbers[index - 1] + list_numbers[index] + list_numbers[index + 1]) // 3  # averaged_number
        smoothed_list.append(averaged_number)  # appends the averaged number to the smoothed_list
    return smoothed_list  # returns the smoothed_list


# Add small test examples in main and run this file to run your own tests.
# Listen to the longer sound clip by running the SoundApp and listen to 
# the effect of the changed sound samples.
def main():
    list_numbers_test_1 = [1, 2, 3]
    list_numbers_test_2 = [8, 9, 11, 53, 62, -21]
    list_numbers_test_3 = [0, 100, 500, -100]
    print('Testing make_reversed_samples([' + str(list_numbers_test_1) + '])')
    print('Expecting to get "[3,2,1]" and got,', make_reversed_samples(list_numbers_test_1))
    print('Testing make_reversed_samples([' + str(list_numbers_test_2) + '])')
    print('Expecting to get "[-21,62,53,11,9,8]" and got,', make_reversed_samples(list_numbers_test_2))
    print('Testing make_reversed_samples([' + str(list_numbers_test_3) + '])')
    print('Expecting to get "[-100, 500, 100, 0]" and got,', make_reversed_samples(list_numbers_test_3))
    print('Testing make_louder_samples([' + str(list_numbers_test_1) + ', 2])')
    print('Expecting to get "[2, 4, 6]" and got,', make_louder_samples(list_numbers_test_1, 2))
    print('Testing make_louder_samples([' + str(list_numbers_test_2) + ', 3])')
    print('Expecting to get "[24, 27, 33, 159, 186, -63]" and got,', make_louder_samples(list_numbers_test_2, 3))
    print('Testing make_louder_samples([' + str(list_numbers_test_3) + ', 4])')
    print('Expecting to get "[0, 400, 2000, -400]" and got,', make_louder_samples(list_numbers_test_3, 4))
    print('Testing make_clipped_samples([' + str(list_numbers_test_1) + ', 2])')
    print('Expecting to get "[1, 2, 2]" and got,', make_clipped_samples(list_numbers_test_1, 2))
    print('Testing make_clipped_samples([' + str(list_numbers_test_2) + ',20 ])')
    print('Expecting to get "[8, 9, 11, 20, 20, -20]" and got,', make_clipped_samples(list_numbers_test_2, 20))
    print('Testing make_clipped_samples([' + str(list_numbers_test_3) + ', 80])')
    print('Expecting to get "[0, 80, 80, -80]" and got,', make_clipped_samples(list_numbers_test_3, 80))
    print('Testing make_clipped_samples([' + str(list_numbers_test_1) + ', 2])')
    print('Expecting to get "[1, 2, 2]" and got,', make_clipped_samples(list_numbers_test_1, 2))
    print('Testing make_noisy_samples([' + str(list_numbers_test_1) + ', 2])')
    print('Expecting to get "[-1 to 3, 0 to 4, 1 to 5]" and got,', make_noisy_samples(list_numbers_test_1, 2))
    print('Testing make_noisy_samples([' + str(list_numbers_test_2) + ', 5])')
    print('Expecting to get "[3 to 13, 4 to 14, 6 to 16, 48 to 58, 57 to 67, -26 to -16]" and got,', make_noisy_samples(list_numbers_test_2, 5))
    print('Testing make_noisy_samples([' + str(list_numbers_test_3) + ', 50])')
    print('Expecting to get "[-50 to 50, 50 to 150, 450 to 550, -150 to -50]" and got,', make_noisy_samples(list_numbers_test_3, 50))
    print('Testing make_smoothed_samples([' + str(list_numbers_test_1) + '])')
    print('Expecting to get "[1,2,2]" and got,', make_smoothed_samples(list_numbers_test_1))
    print('Testing make_smoothed_samples([' + str(list_numbers_test_2) + '])')
    print('Expecting to get "[8, 9, 24, 42, 31, 20]" and got,', make_smoothed_samples(list_numbers_test_2))
    print('Testing make_smoothed_samples([' + str(list_numbers_test_3) + '])')
    print('Expecting to get "[50 200, 166, 200]" and got,', make_smoothed_samples(list_numbers_test_3))


if __name__ == "__main__":
    main()
