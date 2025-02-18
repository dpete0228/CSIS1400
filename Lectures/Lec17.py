def count_ones (string_list):
    one_count = 0
    for string in string_list:
        for char in string:
            if char == '1':
                one_count += 1
    return one_count
def main():
    file = open("example.txt")
    print(file)
    lines = file.readlines()
    print(lines)
    print(count_ones(lines))
    
if __name__ == "__main__":
    main()