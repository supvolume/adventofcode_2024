# AOC 2024 Day 1 Part 1
txt = open("../input/input_day01.txt", 'r').read()
txt_list = list(txt.split("\n"))

first_list = []
second_list = []
for line in txt_list:
    n = line.split("   ")
    first_list.append(int(n[0]))
    second_list.append(int(n[1]))

# Sort
first_list.sort()
second_list.sort()

# Subtract
distance = [abs(a-b) for a, b in zip(first_list, second_list)]
print("Part1: "+sum(distance))
