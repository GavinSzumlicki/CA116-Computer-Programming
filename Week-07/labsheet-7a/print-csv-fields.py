#!/usr/bin/env python3

s = input()
a = []

while s != "end":
  a.append(s)
  s = input()

data = int(input())

count = -1
start = 0
i = 0
while i < len(a) and start < len(a[i]):
  j = start
  while j < len(a[i]) and a[i][j] != ",":
    j = j + 1

  count = count + 1
  if count == data:
    print(a[i][start:j])
    j = -1
    count = -1
    i = i + 1
  start = j + 1
