def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def remove_odd_numbers_version2(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers


name_list = ["Billy", "David", "Joe", "David", "Javier", "Hayden", "Jimmy", "David", "John"]
name_list = [name for name in name_list if name != "David"]
print(name_list)
