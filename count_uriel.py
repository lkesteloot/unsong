
# python3 count_uriel.py unsong-1.md

import sys

line_number = 0
filename = sys.argv[1]
for line in open(filename):
    line = line.strip()
    line_number += 1

    if line.startswith("#"):
        continue

    letter_count = 0
    cap_count = 0

    first_cap = 0
    for col, ch in enumerate(line):
        if ch >= "A" and ch <= "Z":
            cap_count += 1
            letter_count += 1
            if first_cap == 0:
                first_cap = col
        if ch >= "a" and ch <= "z":
            letter_count += 1

    if letter_count > 0 and cap_count > letter_count * 0.5:
        print("%s:%d:%d: %s" % (filename, line_number, first_cap + 1, line))

