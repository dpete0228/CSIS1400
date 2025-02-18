def odd(number):
    return number%2 == 1


def delete_odd_numbers_from_list(number_list):
    even_list = []
    for index in range(len(number_list)):
        if not odd(number_list[index]):
            even_list.append(number_list[index])
            print (even_list)
    return even_list

def main():
    numbers = list(range(10))
    print(delete_odd_numbers_from_list(numbers))
if __name__ == "__main__":
    main()