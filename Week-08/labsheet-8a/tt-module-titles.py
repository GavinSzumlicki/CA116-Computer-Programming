#!/usr/bin/env python3

tt_entry = input()

while tt_entry != "end":
  print(" ".join(tt_entry.split()[5:]))
  tt_entry = input()
