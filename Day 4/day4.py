import re
# Count number of valid passports
file = open("input.txt", "r")
lines = file.readlines()


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
        fields = s.split(' ')
        passports.append(fields)
        s = ""
for n in passports:
    for k in n:
        if k == '':
            n.remove(k)
validated_passports = []
for pas in passports:
    if len(pas) == 8:
        part1 += 1
        validated_passports.append(pas)
    if len(pas) == 7:
        valid = True
        for n in pas:
            if 'cid' in n:
                valid = False
        if valid:
            part1 += 1
            validated_passports.append(pas)
print(len(validated_passports))
for i in validated_passports:
    valid = True
    for j in i:
        key = re.search(r'(.*):', j).group(1)
        value = re.search(r'^.+:(.+)$', j).group(1)
        if key == 'byr' and not 1920 <= int(value) <= 2002:
            valid = False
        if key == 'iyr' and not 2010 <= int(value) <= 2020:
            valid = False
        if key == 'eyr' and not 2020 <= int(value) <= 2030:
            valid = False
        if key == 'hgt':
            height = re.search(r':(\d*)', j).group(1)
            if j.endswith('cm') and not 150 <= int(height) <= 193:
                valid = False
            elif j.endswith('in') and not 59 <= int(height) <= 76:
                valid = False
        if key == 'hcl':
            haircolor = re.search(r':(.*)', j).group(1)
            if haircolor[0] != '#' or any([c not in '0123456789abcdef' for c in haircolor[1:]]) or len(haircolor.strip("#")) != 6:
                valid = False
        if key == 'ecl':
            colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value not in colors:
                valid = False
        if key == 'pid':
            if not value.isnumeric() or not len(value) == 9:
                valid = False
    if valid:
        part2 += 1


print("Part 1:", part1)
print("Part 2:", part2)
