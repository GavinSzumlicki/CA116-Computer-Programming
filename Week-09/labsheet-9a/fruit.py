#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
fruit = {
  "apple": True,
  "pear": True,
  "orange": True,
  "banana": True,
  "cherry": True,
}

i = 0
while i < len(words):
  if words[i].strip() in fruit:
    print(words[i].strip())
  i = i + 1
