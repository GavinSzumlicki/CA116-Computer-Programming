#!/usr/bin/env python3

tt_entry = input()

while tt_entry != "end":
  if 1 < int(tt_entry.split()[2]):
    print(tt_entry)
  tt_entry = input()
