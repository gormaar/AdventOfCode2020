import re
# Count number of valid passports
file = open("input.txt", "r")
lines = file.readlines()


def day4():
    part1 = 0
    part2 = 0
    passports = []
    s = ""
    lines.append("\n")
    for line in lines:
        if line != '\n':
            strippedLine = line.replace('\n', ' ')
            s += strippedLine
        else:
            props = s.split(' ')
            passports.append(props)
            s = ""
    for n in passports:
        for k in n:
            if k == '':
                n.remove(k)
    valid_passports = 0
    for i in passports:
        if len(i) == 8 or len(i) == 7 and 'cid' not in i:
            part1 += 1
            for j in i:
                value = re.search(r'^.+:(.+)$', j).group(1)
                if 'byr' in j and 1920 <= int(value) <= 2002:
                    valid_passports += 1
                if 'iyr' in j and 2010 <= int(value) <= 2020:
                    valid_passports += 1
                if 'eyr' in j and 2020 <= int(value) <= 2030:
                    valid_passports += 1
                if 'hgt' in j:
                    if not j.islower():
                        pass
                    measure = j[-2:]
                    height = value[:-2]
                    if measure == 'cm':
                        if 150 <= int(height) <= 193:
                            valid_passports += 1
                    elif measure == 'in':
                        if 59 <= int(height) <= 76:
                            valid_passports += 1
                if 'hcl' in j:
                    haircolor = re.search(r':(.*)', j).group(1)
                    if len(haircolor) == 7:
                        valid_passports += 1
                if 'ecl' in j:
                    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if value in colors:
                        valid_passports += 1
                if 'pid' in j:
                    if len(str(value)) == 9:
                        valid_passports += 1
                if valid_passports == 7:
                    part2 += 1
                    valid_passports = 0

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    day4()
