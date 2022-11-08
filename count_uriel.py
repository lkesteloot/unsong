
# python3 count_uriel.py < unsong-1.md

import sys

for line in sys.stdin:
    line = line.strip()

    if line.startswith("#"):
        continue

    letter_count = 0
    cap_count = 0

    for ch in line:
        if ch >= "A" and ch <= "Z":
            cap_count += 1
            letter_count += 1
        if ch >= "a" and ch <= "z":
            letter_count += 1

    if letter_count > 0 and cap_count > letter_count * 0.5:
        print(line)

