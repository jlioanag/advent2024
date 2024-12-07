import re

PREFIX = 'mul('
SUFFIX = ')'

with open('day3-input.txt', 'r+') as f:
    sum = 0
    for line in f:
        muls = re.findall(r"(mul\(\d{1,},\d{1,})\)", line)
        
        for x in muls:
            n = x.replace('mul(', '').split(',')
            sum += (int(n[0]) * int(n[1]))
    print(sum)