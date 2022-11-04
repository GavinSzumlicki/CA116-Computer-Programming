#!/usr/bin/env python3

s = input()
seen = []

while s != "end":
  i = 0
  while i < len(seen) and s != seen[i]:
    i = i + 1
  if i == len(seen):
    print(s)
  seen.append(s)
  s = input()
