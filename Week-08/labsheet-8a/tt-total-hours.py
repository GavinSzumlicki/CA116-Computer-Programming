#!/usr/bin/env python3

tt_entry = input()
total = 0

while tt_entry != "end":
  total = total + int(tt_entry.split()[2])
  tt_entry = input()

print(total)
