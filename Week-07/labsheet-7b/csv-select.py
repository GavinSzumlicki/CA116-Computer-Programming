#!/usr/bin/env python3

import sys
args = sys.argv[1]

i = 0
while i < len(args) and args[i] != "=":
  i = i + 1

header = args[:i]
value = args[i + 1:]


s = input()
a = []

while s != "end":
  a.append(s)
  s = input()

i = 0
while i < len(a[0].split(",")):
  if header == a[0].split(",")[i]:
    num = i
  i = i + 1

i = 0
while i < len(a):
  if a[i].split(",")[num] == value:
    print(a[i])
  i = i + 1
