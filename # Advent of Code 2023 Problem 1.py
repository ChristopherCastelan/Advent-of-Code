# Advent of Code 2023 Problem 1
import re

Handle = open(str(input("File:").strip('""')))
    
x = 0
y = 0

total_amount = []

for lines in Handle:
    line = re.sub('\D', '', lines)
    nums = [z for z in line]
    x = nums[0]
    if len(nums) > 1: 
        y = nums[-1]
    else: 
        y = nums[0]
    lst = [x, y]
    totals = ''.join(lst)
    total_amount.append(int(totals))
    
print(sum(total_amount))



    