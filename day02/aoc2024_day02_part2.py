# AOC 2024 Day 2 Part 2
txt = open('../input/input_day02.txt', 'r').read()
txt_list = list(txt.split('\n'))

count = 0

def safe_check(level_list):
    safe = len(level_list)-1 # to count unsafe gap
    
    if (level_list == sorted(level_list)) or (level_list == sorted(level_list,reverse=True)):
        for i in range(0, len(level_list)-1):
            if abs(level_list[i]-level_list[i+1]) not in [1,2,3]:
                break
            else:
                safe -= 1
                
    if safe == 0:
        return 1
    return 0


for report in txt_list:
    level_list = report.split(' ')
    level_list = [int(i) for i in level_list]
    if safe_check(level_list) == 1:
        count += 1
    else:
        for i in range(0, len(level_list)):
            new_level = level_list.copy()
            new_level.pop(i)
            if safe_check(new_level) == 1:
                count += 1
                break

print("Part2: " + str(count))
