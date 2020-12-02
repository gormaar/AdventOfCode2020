import re

# Find amount of valid passwords according to policies

file = open("input.txt", "r")
passwords = file.readlines()


def day1_part1():
    ans = 0
    for line in passwords:
        letter = re.search(r'([a-z]+):', line).group(1)
        pw = re.search(r': ([a-z]+)', line).group(1)
        digits = re.findall(r'\d+', line)
        count = 0
        for l in pw:
            if l == letter:
                count += 1
        if int(digits[0]) <= count <= int(digits[1]):
            ans += 1
    print("Part 1:", ans)


def day1_part2():
    ans = 0
    for line in passwords:
        letter = re.search(r'([a-z]+):', line).group(1)
        pw = re.search(r': ([a-z]+)', line).group(1)
        digits = re.findall(r'\d+', line)
        list(pw)
        hi, lo = int(digits[1]), int(digits[0])
        if letter == pw[hi-1] and letter != pw[lo-1]:
            ans += 1
        elif letter == pw[lo-1] and letter != pw[hi-1]:
            ans += 1
    print("Part 2:", ans)


if __name__ == '__main__':
    day1_part1()
    day1_part2()
