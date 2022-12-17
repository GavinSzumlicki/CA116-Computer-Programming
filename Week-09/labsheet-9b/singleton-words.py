#!/usr/bin/env python3

import sys
data = sys.stdin.readlines()

seen = []
dupe = []

i = 0
while i < len(data):
  if data[i] not in seen and data[i] not in dupe:
    seen.append(data[i])
  else:
    dupe.append(data[i])
  i = i + 1

i = 0
while i < len(data):
  if data[i] in seen and data[i] not in dupe:
    print(data[i].rstrip())
  i = i + 1
