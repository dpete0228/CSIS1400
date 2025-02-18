def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_numbers(numbers[1:])

def main():
    print(sum_numbers([1, 2, 3, [4, 5]]))


if __name__ == "__main__":
    main()