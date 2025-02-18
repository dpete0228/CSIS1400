def is_word_in_list(word_to_find, words):
    for word in words:
        if word == word_to_find:
            return True
    return False

print('Testing is_word_in_list("Sally", ["David", "Sally", "Maria"]). Expect True and got', is_word_in_list("Sally", ["David", "Sally", "Maria"]))