#!/usr/bin/env python3

tt_entry = input()
tt = []

while tt_entry != "end":
  tt.append(tt_entry)
  tt_entry = input()

day = input()

i = 0
while i < len(tt):
  if tt[i][0] == day:
    print(tt[i])
  i = i + 1
