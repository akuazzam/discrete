def generate_pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to the specified number of rows.
    :param rows: Number of rows in the triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
    triangle = []
    for i in range(rows):
        row = [1]  # Start with 1
        if triangle:  # If not the first row, calculate based on the previous row
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # End with 1
        triangle.append(row)
    return triangle


def display_pascals_triangle(triangle):
    """
    Display Pascal's Triangle in a readable format.
    :param triangle: The list of lists representing Pascal's Triangle.
    """
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width))


if __name__ == "__main__":
    # Ask user for the number of rows
    rows = int(input("Enter the number of rows for Pascal's Triangle: "))
    if rows <= 0:
        print("Please enter a positive integer.")
    else:
        pascals_triangle = generate_pascals_triangle(rows)
        print("\nPascal's Triangle:")
        display_pascals_triangle(pascals_triangle)
        print("\nExplanation:")
        print("- Each row represents coefficients in the binomial expansion.")
        print("- The numbers in the triangle also represent combinations (n choose k).")
        print("- For example, the 3rd row (1 2 1) represents n=2: (2 choose 0), (2 choose 1), and (2 choose 2).")
