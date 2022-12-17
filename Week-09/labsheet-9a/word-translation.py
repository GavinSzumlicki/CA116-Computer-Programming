#!/usr/bin/env python3

import sys
a = sys.stdin.readlines()

file_name = "translation.txt"
with open(file_name) as f:
  data = f.readlines()

i = 0
while i < len(a):
  j = 0
  while j < len(data):
    if a[i].strip() == data[j][0:len(a[i].rstrip())]:
      print(data[j][len(a[i].strip()) + 1:].rstrip())
    j = j + 1
  i = i + 1
