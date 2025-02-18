# This computes a single row of a multiplication table. It returns a list
# that is [1*row_value, 2 * row_value,...,number_of_columns*row_value].
def compute_a_multiplication_table_row(row_value, number_of_columns):
    row_list = []
    for column_value in range(1, number_of_columns + 1):
        entry = row_value * column_value
        row_list.append(entry)
    return row_list


# This makes a multiplication table num_columns entries across and
# num_rows rows in the table. Calling make_multiplication_table(2,3)
# will return a list containing 2 elements. Each element is itself
# a list with 3 elements. Thus, each row is a list and the table
# is a list of lists. A 2 x 3 table should look like
# [[1, 2, 3], [2, 4, 6]]
def make_multiplication_table(num_rows, num_columns):
    table = []
    for row in range(1, num_rows + 1):
        row_list = compute_a_multiplication_table_row(row, num_columns)
        table.append(row_list)
    return table


# This function prints out the table so that the columns stay lined up.
# Each value in the table is padded to take up 5 spaces.
# The table should be a list of rows, where each row is a list of values.
# A 2 x 3 table parameter should look like
# [[1, 2, 3], [2, 4, 6]]
def print_multiplication_table(table):
    for row in table:
        for value in row:
            # print value with padding to make 5 spaces
            print(value, end='\t')
        print()  # add a newline at the end of the row


# Define the size of a multiplication table, create it, and print it in a formatted way.
def main():
    # define the size of the table
    number_of_rows = 3
    number_of_columns = 4

    # make the table
    table = make_multiplication_table(number_of_rows, number_of_columns)
    print(table)

    # output the table
    print("A", number_of_rows, "x", number_of_columns, "multiplication table")
    print_multiplication_table(table)


if __name__ == "__main__":
    main()
