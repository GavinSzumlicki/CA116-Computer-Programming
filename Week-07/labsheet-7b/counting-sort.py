#!/usr/bin/env python3

data = []
count = {}
n = input()
while n != "end":
  count[n] = count.get(n, 0) + 1
  n = input()

i = 0
while i < 1000:
  if str(i) in count:
    curr = (str(i) + "\n") * int(count[str(i)])
    print(curr.rstrip())
  i = i + 1
