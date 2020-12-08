# Calculate the higherst seat ID on a boarding pass
import math
file = open("input.txt", "r")
lines = file.readlines()

boardingpasses = []
ans = 0
for boardingpass in lines:
    row, col = 0, 0
    row_len, col_len = 127, 7
    boardingpass.strip()
    for letter in boardingpass:
        if letter == 'F':
            row_len /= 2
            row_len += row/2
            row_len = int(row_len)
        elif letter == 'B':
            row += (row_len/2)-(row/2)
            row = math.ceil(row)
        if letter == 'R':
            col += (col_len/2)-(col/2)
            col = math.ceil(col)
        elif letter == 'L':
            col_len /= 2
            col_len += col/2
            col_len = int(col_len)
    boardingpass_id = row*8+col
    boardingpasses.append(boardingpass_id)
    ans = max(ans, boardingpass_id)
print(ans)

for boardingpass in lines:
    row, col = 0, 0
    row_len, col_len = 127, 7
    boardingpass.strip()
    for letter in boardingpass:
        if letter == 'F':
            row_len /= 2
            row_len += row/2
            row_len = int(row_len)
        elif letter == 'B':
            row += (row_len/2)-(row/2)
            row = math.ceil(row)
        if letter == 'R':
            col += (col_len/2)-(col/2)
            col = math.ceil(col)
        elif letter == 'L':
            col_len /= 2
            col_len += col/2
            col_len = int(col_len)
    boardingpass_id = row*8+col
    if boardingpass_id - 1 not in boardingpasses:
        print("My boardingpassID", boardingpass_id-1)
    elif boardingpass_id + 1 not in boardingpasses:
        print("My boardingpassID", boardingpass_id+1)