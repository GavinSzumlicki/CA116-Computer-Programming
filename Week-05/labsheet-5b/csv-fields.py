#!/usr/bin/env python3

header = input()
start = 0

i = 0
while start < len(header):
  j = start
  while j < len(header) and header[j] != ",":
    j = j + 1

  print(header[start:j])
  start = j + 1

  i = i + 1
