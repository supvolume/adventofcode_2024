# AOC 2024 Part 2
txt = open("../input/input_day01.txt", 'r').read()
txt_list = list(txt.split("\n"))

first_list = []
second_list = []
for line in txt_list:
    n = line.split("   ")
    first_list.append(int(n[0]))
    second_list.append(int(n[1]))

# Check number of appearance on the right
right_appear = {}
for i in second_list:
    if i not in right_appear:
        right_appear[i] = 1
    else:
        right_appear[i] += 1

score = 0

for i in first_list:
    if i in right_appear:
        score += i*right_appear[i]

print("Part2: "+str(score))
