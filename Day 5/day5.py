# Calculate the higherst seat ID on a boarding pass
file = open("input.txt", "r")
lines = file.readlines()

def day5():
    ans = 0
    row = 0
    half_row = 64
    col = 0
    half_col = 4
    for boardingpass in lines:
        boardingpass = boardingpass.strip()
        for letter in boardingpass:
            if letter == 'F':
                row += half_row
            row /= 2
            if letter == 'R':
                col += half_col
                half_row /= 2
            elif letter == 'L':
                half_col /= 2
            id = row*8+col
            ans = max(ans, id)
    print(ans)


if __name__ == '__main__':
    day5()
