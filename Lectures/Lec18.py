# def words_without_periods(list_sentences):
#     split_list = []
#     for sentence in list_sentences:
#         words = sentence.split()
#         if words[-1][-1] == ".":
#             words[-1] = words[-1][:-1]
#         split_list += words
#     print(split_list)
def evaluate(cash):
    if cash > 90:
        return 'high'
    elif cash > 80:
        return 'upper mid'
    elif cash > 70:
        return 'mid'
    else:
        return 'low'
def kind_of_loop(values):
    for index in range(1, len(values)):
        if values[index] > values[index-1]:
            return index
def sum_values(numbers):
    """
    Computes the sum of all the values in numbers
    :param numbers: A list of numbers
    :return: The sum of the list of number
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum
def change(x):
    x['a'] = 1
    return x

def main():
    # words_without_periods(['i like cats.', 'my name is David.', 'I am Mr. Peters'])
    print(sum_values([2, 1, 5, 4]))
    print(sum_values([]))
    print(kind_of_loop([5, 4, 2, 1, 1]))
    y = {'b': 2}
    change(y)
    print(y)
if __name__ == "__main__":
    main()