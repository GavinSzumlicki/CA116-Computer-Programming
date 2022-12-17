#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
seen = {}

i = 0
while i < len(words):
  if words[i] not in seen:
    seen[words[i]] = True
  else:
    print("snap:", words[i].rstrip())
    i = len(words)
  i = i + 1
