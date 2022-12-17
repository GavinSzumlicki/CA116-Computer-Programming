#!/usr/bin/env python3

import sys
a = sys.stdin.readlines()

correct = []

i = 0
while i < len(a):

  corr = a[i].rstrip()[len(a[i]) - 9:]
  corr2 = a[i].rstrip()[:len(a[i]) - 9]

  if corr == ".correct" and corr2 not in correct:
    correct.append(a[i].rstrip()[:len(a[i]) - 9])
  if corr == ".correct" and corr2 in correct:
    pass
  elif a[i].split(".")[0] + "." + a[i].split(".")[1] in correct:
    j = 0
    while j < len(correct):
      if correct[j] == a[i].split(".")[0] + "." + a[i].split(".")[1]:
        correct.remove(correct[j])
      j = j + 1
  i = i + 1
print("\n".join(correct))
