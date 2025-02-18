def check_for_equal_neighbors(values):
    last = None
    for value in values:
        if last == value:
            return True
        last = value
    return False

def main():
    print(check_for_equal_neighbors([3, 2, 1]))
    vals = [1, 2, 3]
    vals = [val + val for val in [val+1 for val in vals]]
    print (vals)


if __name__ == "__main__":
    main()