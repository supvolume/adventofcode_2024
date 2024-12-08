# AOC 2024 Day 3 Part 1
import re

txt = open('../input/input_day03.txt', 'r').read()

mul_sum = 0

mul_list = re.findall('mul\(\d+,\d+\)', txt)
mul_num = [x[4:-1] for x in mul_list]
for mul in mul_num:
    i,j = mul.split(',')
    mul_sum += int(i)*int(j)

print('Part1: '+ str(mul_sum))
    
