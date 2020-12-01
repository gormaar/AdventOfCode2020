# Multiply expenses that add up to 2020 from expense report


file = open("input.txt", "r")
expenses = file.readlines()


def day1_part1():
    for expense1 in expenses:
        for expense2 in expenses:
            if int(expense1) + int(expense2) == 2020:
                print("Part1", int(expense1) * int(expense2))
                return


def day1_part2():
    for expense1 in expenses:
        for expense2 in expenses:
            for expense3 in expenses:
                if int(expense1) + int(expense2) + int(expense3) == 2020:
                    print("Part2", int(expense1) * int(expense2) * int(expense3))
                    return


if __name__ == '__main__':
    day1_part1()
    day1_part2()
