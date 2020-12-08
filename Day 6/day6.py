#Count sum of yes-answers

file = open("input.txt", "r")
lines = file.readlines()
lines.append('\n')
ans = 0
unique_answers = []
for line in lines:
    if line != '\n':
        for letter in line:
            if letter not in unique_answers and letter != '\n':
                unique_answers.append(letter)
    else:
        ans += len(unique_answers)
        unique_answers.clear()
print(ans)
