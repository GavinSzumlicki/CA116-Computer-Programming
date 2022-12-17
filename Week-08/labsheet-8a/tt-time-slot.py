#!/usr/bin/env python3

tt_entry = input()


while tt_entry != "end":
  start = int(tt_entry.split()[1])
  end = (int(start) - 1 + int(tt_entry.split()[2])) % 24
  duration = (str(start) + ":00", str(end) + ":50")
  duration = " ".join(duration)

  print(tt_entry.split()[0], duration, " ".join(tt_entry.split()[3:]))
  tt_entry = input()
