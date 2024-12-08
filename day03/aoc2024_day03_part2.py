# AOC 2024 Day 3 Part 2
import re

txt = open('../input/input_day03.txt', 'r').read()

mul_sum = 0
mul_list = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", txt)
active = 1

for order in mul_list:
    if order == "don't()":
        active = 0
    elif order == "do()":
        active = 1
    elif active == 1:
        i,j = order[4:-1].split(',')
        mul_sum += int(i)*int(j)

print('Part2: '+ str(mul_sum))
    

