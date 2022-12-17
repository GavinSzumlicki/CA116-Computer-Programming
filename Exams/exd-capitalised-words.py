#!/usr/bin/env python3

import sys
text = sys.stdin.read()

words = text.split("\n")
words = " ".join(words)
words = words.split(" ")

new_words = []
i = 0
while i < len(words):
  if len(words[i]) != 0:
    new_words.append(words[i])
  i = i + 1

i = 0
while i < len(new_words):
  if new_words[i][0] <= "Z" and "A" <= new_words[i][0]:
    print(new_words[i])
  i = i + 1
