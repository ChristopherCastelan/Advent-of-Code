# Advent of Code Problem 2 
# Python
import re

Handle = open(str(input("File:").strip('""')))

pattern = r'[:,;]'

def duplicates(seq, item): 
    Start = -1 
    locs = []
    while True: 
        try: 
            loc = seq.index(item, Start+1)
        except ValueError: 
            break
        else: 
            locs.append(loc)
            Start = loc
    return locs

lst = []

for lines in Handle: 
    line = re.split(pattern, lines)
    Games = "".join(line)
    if Games.startswith("Game"):
        colors = Games.split()
        red_count = 0
        blue_count = 0
        green_count = 0
        for z in duplicates(colors, 'red'): 
            red_count += int(colors[z - 1]) 
        for z in duplicates(colors, 'blue'): 
            blue_count += int(colors[z - 1]) 
        for z in duplicates(colors, 'green'): 
            green_count += int(colors[z - 1]) 
        if red_count < 12 and blue_count < 14 and green_count < 13: 
            lst.append(int(colors[1]))

print(sum(lst))
    
