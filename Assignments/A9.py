"""
Initial code by David Johnson. This code and derived works may not be posted publicly.

Code finished by
"""

# Add your critical thinking sentences and example review as described in the assignment here.
"""
The program overall, does a good job of predicting movie reviews. The only problem is that it of course doesn't have a 
guess at what some good/bad words are and whether they should be considered good or bad so they're just None. As a result
those words don't count towards the overall score of the review. My negative review was: 
I want to gouge my eyes out
I got a predicted review score of 3.16. This is obviously not what the review should read. But looking into it, the only 
word that didn't return None, was eyes, with a rating of 3.16. So the overall review got a 3.16.
"""
# Add your functions here.
def make_lowercase_lines_from_file(filename):
    """
    Takes a file and makes all the characters lowercase
    :param filename: a file with movie reviews
    :return: the now lowercase lines from the file
    """
    file = open(filename)  # Open the file
    lines = file.readlines()  # Saves all the lines from the file in a list
    for index in range(len(lines)):  # Goes through each index of the list and sets each string to lowercase
        lines[index] = lines[index].lower()
    return lines

def make_word_total_value_dict_from_lines(string_list):
    """
    Accumulates the value of various strings
    :param string_list: a list of strings
    :return: the value dictionary
    """
    dictionary = {}
    for string in string_list:  # Look at each string in the list
        word_list = string.split()  # Splits each string into individual words
        value = int(word_list[0])  # The initial number of each string is the associate value for each word
        word_list = word_list[1:]  # Looks at the rest of the string, not the first value
        for word in word_list:  # Look at each word
            dictionary[word] = dictionary.get(word, 0) + value  # Either initialize or add the value of the word
    return dictionary

def make_word_total_count_dict_from_lines(string_list):
    """
    Counts the number of times a given word is in all of the reviews
    :param string_list: A list of strings
    :return: the count dictionary
    """
    count = {}
    for string in string_list:  # Looks at each string in the list
        word_list = string.split()  # Splits the string
        word_list = word_list[1:]  # The initial character is the value of each word and is not needed
        for word in word_list:  # Looking at each word
            count[word] = count.get(word, 0) + 1  # Adds one to count each time it finds a given word
    return count

def make_word_avg_value_from_total_and_count(word_total_dict, word_count_dict):
    """
    Finds the average review for each word
    :param word_total_dict: The accumulated value of each given word
    :param word_count_dict: The number of times a given word is in the review
    :return: The average value of each word
    """
    word_avg_dict = {}
    for key in word_total_dict:  # Looks at each value in the total dictionary (same as the count)
        average = word_total_dict.get(key) / word_count_dict.get(key)  # Takes the average
        if average < 1.75 or average > 2.25:  # If it's around 2 then it means the word is common in all the reviews
            word_avg_dict[key] = average
    return word_avg_dict

def predict_review (review_string, word_avg_dict):
    """
    Predicts the overall rating given the words in a review
    :param review_string: The given review to look at
    :param word_avg_dict: The dictionary of the average value of each word
    :return:
    """
    words = review_string.split() # Splits the string into individual words
    total = 0
    count = 0
    for word in words:  # Look at each individual word
        if word in word_avg_dict:  # if the word is in the dictionary
            count += 1  # Adds one to count
            total += word_avg_dict[word]  # Adds the average value of the word
    predicted_rating = total/count  # Finding the average of all the given words in a review
    return predicted_rating



# This function is provided for you to use.
def compare_prediction_with_actual(lines, avg_value_dict):
    """
    Given a list of movie reviews and a dictionary of words and their average value, compare
    the predicted with the actual rating.
    :param lines: a list of movie reviews. Each review starts with a 0 to 4 movie rating.
    :param avg_value_dict: A diction\ary of words and their average value in a movie review rating
    :return: None. This prints out some predicted and actual score for movie reviews.
    """
    for line in lines:
        words = line.split()
        actual_score = int(words[0])
        predicted_score = predict_review(" ".join(words[1:]), avg_value_dict)
        print("predicted:", predicted_score, "actual:", line)

def main():
    """
    Read a file of movie reviews, develop a dictionary of word values, and use
    those to make movie rating predictions.
    """
    # Add some testing code below here. Make a small list of reviews by hand or read in a small
    # file. Make small total value and count dictionaries to test the average function. Make a small
    # average dictioanry to test the prediction function. Make these by hand to make the tests be as independent
    # from each other as possible. Do not just make a list of reviews and then call each function in order.

    string_list_1 = ["1 how are you doing", "2 i am doing fine", "3 how are you", "4 i am doing great"]
    dict_1 = {'how': 3, 'when': 8, 'now': 6, 'then': 2}
    dict_2 = {'how': 1, 'when': 3, 'now': 2, 'then': 1}
    avg_dict = {'how': 3.0, 'are': 2.0, 'doing': 4.0, 'when': 2.6666666666666665, 'now': 3.0}
    # Testing make_word_total_value_dict_from_lines
    print("Testing make_word_total_value_dict_from_lines(string_list_1), expecting {'how': 4, 'are': 4, 'you': 4, "
          "'doing': 7, 'i': 6, 'am': 6, 'fine': 2, 'great': 4},")
    print("and got", make_word_total_value_dict_from_lines(string_list_1))

    # Testing make_word_total_count_dict_from_lines
    print("Testing make_word_total_count_dict_from_lines(string_list_1), expecting {'how': 2, 'are': 2, 'you': 2, "
          "'doing': 3, 'i': 2, 'am': 2, 'fine': 1, 'great': 1}")
    print("and got", make_word_total_count_dict_from_lines(string_list_1))

    # Testing make_word_avg_value_from_total_and_count
    print("Testing make_word_avg_value_from_total_and_count(dict_1, dict_2, expecting {'how': 3.0, "
          "'when': 2.6666666666666665, 'now': 3.0}")
    print("and got", make_word_avg_value_from_total_and_count(dict_1, dict_2))

    # Testing predict_review
    print("Testing predict_review('how are you doing', avg_dict), expecting 3.0")
    print("and got", predict_review('how are you doing', avg_dict))
    # read the reviews into a list
    # lines = make_lowercase_lines_from_file("smallReviews.txt")
    lines = make_lowercase_lines_from_file("MovieReviews.txt") # uncomment this when you are ready to try the full set of reviews.
    # print(lines)  # examine the result
#     # Make a dict with words from reviews and their summed up values from the reviews they are in
    total_value_dict = make_word_total_value_dict_from_lines(lines)
    # print(total_value_dict) # examine the dict to see if it looks correct
#
#     # Count up how often a word appears in all the reviews
    total_count_dict = make_word_total_count_dict_from_lines(lines)
    # print(total_count_dict) # examine the dict to see if it looks correct
#
#     # Get the average value per word from the total value and their count
    avg_value_dict = make_word_avg_value_from_total_and_count(total_value_dict, total_count_dict)
    # print(avg_value_dict) # examine the dict to see if it looks correct
#
#     # Compare actual and predicted movie ratings for a small number of reviews
    if len(lines) < 110:
        compare_prediction_with_actual(lines, avg_value_dict) # use all for small review files
    else:
        compare_prediction_with_actual(lines[100:110], avg_value_dict)
#
#     # Ask the user for a movie review and predict a rating. It should be without punctuation.
    personal_movie_review = input("Please enter a review with no punctuation: ")
    personal_movie_review = personal_movie_review.lower()
    prediction = predict_review(personal_movie_review, avg_value_dict)
    print("The predicted review score is", prediction)

if __name__=="__main__":
    main()
