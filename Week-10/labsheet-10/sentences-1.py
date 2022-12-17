#!/usr/bin/env python3

import sys

a = sys.stdin.read()
a = a.split("\n")
a = " ".join(a)
a = a.split(" ")

words = []
i = 0
while i < len(a):
  if len(a[i]) != 0:
    words.append(a[i])
  i = i + 1
text = " ".join(words)

text = text.split(". ")
text = ".\n".join(text)

text = text.split("? ")
text = "?\n".join(text)

text = text.split("! ")
text = "!\n".join(text)
print(text)
