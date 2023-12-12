# Advent of Code 2023 Problem 1
Handle = open(str(input("File:").strip('""')))
x = 0

for lines in Handle:
    Numbers = []
    for line,nums in enumerate(lines): 
        if nums.isdigit():
            Numbers.append(nums)
        for newnums,equals in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if lines[line:].startswith(equals):
                Numbers.append(str(newnums+1))
    x += int(Numbers[0]+Numbers[-1])

print(x)
            