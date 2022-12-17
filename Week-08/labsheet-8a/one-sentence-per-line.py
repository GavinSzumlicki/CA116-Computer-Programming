#!/usr/bin/env python3

line = input()
all_lines = []

while line != "end":
  line = line.strip()
  all_lines.append(line)
  line = input()

all_lines = " ".join(all_lines)
all_lines = all_lines.split()
all_lines = " ".join(all_lines)

all_lines = all_lines.split(".")

i = 0
while i < len(all_lines):
  all_lines[i] = all_lines[i].strip()
  if 0 < len(all_lines[i]):
    print(all_lines[i] + ".")
  i = i + 1
