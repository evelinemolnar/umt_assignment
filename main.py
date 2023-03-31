from math import factorial

'''
The solution to solving this problem was:
- traverse through every point and group elements by x-coordinate and y-coordinate
- loop over all pairs of x coordinates
- using nested loops to work with two x-coordinates
- find the common y-coordinates between the two coordinates
- use the combinations formula to find the number of rectangles between the 2 x-coordinates and the common y-coordinates that we have found
- keep traversing all other points until we get to the end
- the overall complexity is o(n^2)
'''


def count_rectangles(points):
    # Group the points by x-coordinate and y-coordinate
    x_to_y = {}
    y_to_x = {}
    for x, y in points:
        x_to_y.setdefault(x, []).append(y)
        y_to_x.setdefault(y, []).append(x)

    count = 0
    # Loop over all pairs of x-coordinates
    for x1 in sorted(x_to_y):
        for x2 in sorted(x_to_y):
            if x2 <= x1:
                continue
            # Find the common y-coordinates between the two x-coordinates
            y1_set = set(x_to_y[x1])
            y2_set = set(x_to_y[x2])
            common_y = sorted(list(y1_set & y2_set))
            # Calculate how many coordinates y they have in common by the length of the list
            length = len(common_y)
            if length >= 2:  # Condition if they have common coordinates
                # Using the combinations formula to find how many rectangles we can find with the two x-coordinates
                # and the common y-coordinates ( we choose two y coord out of all the common y coord)
                count = count + (factorial(length) / (factorial(2) * factorial(length - 2)))

    return round(count)  # round the result because we use this variable with division,
    # our count variable becomes float and we want to return integer


# test with the provided input
print(count_rectangles([[1, 1], [1, 3], [2, 1], [3, 1], [2, 3], [3, 3]]))
