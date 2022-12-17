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

final = []
capitals = text.split("\n")
i = 0
while i < len(capitals):
  caps = capitals[i].split(" ")
  print(caps[0][0].capitalize() + caps[0][1:], " ".join(caps[1:]))
  i = i + 1
