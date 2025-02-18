def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0
    sum = numbers[0] + sum_numbers(numbers[1:])
    return sum

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)
def reverse_list(values):
    if len(values) == 0:
        return values
    return [values[-1]] + reverse_list(values[0:-1])

def main():
    print(sum_numbers([1, 2, 3, 4, 5]))
    print(factorial(6))
    print(reverse_list([1,2,3,4,5]))
    print(fibo(20))

if __name__ == "__main__":
    main()