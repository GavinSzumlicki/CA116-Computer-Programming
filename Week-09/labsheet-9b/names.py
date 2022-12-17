#!/usr/bin/env python3

import sys
names = sys.stdin.readlines()

with open("boys.txt") as f:
  boys = f.readlines()

with open("girls.txt") as f:
  girls = f.readlines()


i = 0
while i < len(names):
  if names[i] in boys and names[i] in girls:
    print(names[i].rstrip(), "either")
  elif names[i] in boys:
    print(names[i].rstrip(), "boy")
  else:
    print(names[i].rstrip(), "girl")
  i = i + 1
