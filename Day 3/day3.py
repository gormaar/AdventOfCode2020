# Calculate amount of trees encountered in a slope of 3 right 1 down
file = open("input.txt", "r")
lines = file.readlines()


def day3(x, y):
    trees, x_index, matrix = 0, 0, []
    [matrix.append(line.strip()) for line in lines]
    for n, slope in enumerate(matrix[y:]):
        if n % y == 0:
            x_index += x
            if x_index > len(slope)-1:
                x_index -= len(slope)
            if slope[x_index] == "#":
                trees += 1
            pass
    return trees


if __name__ == '__main__':
    print("Part 1:", day3(3, 1))
    print("Part 2:", day3(1, 1) * day3(3, 1) * day3(5, 1) * day3(7, 1) * day3(1, 2))