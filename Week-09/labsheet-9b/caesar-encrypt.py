#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
encrypt = []
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

dictionary = {}

i = 0
while i < len(src):
  dictionary[i] = dst[i]
  i = i + 1

k = 0
while k < len(words):
  encrypt = []
  i = 0
  while i < len(words[k]):
    letter = "".join([words[k]])[i]
    j = 0
    while j < len(src):
      if src[j] == letter:
        encrypt.append(dictionary[j])
        j = len(src)
      j = j + 1
    if j == len(src):
      encrypt.append(letter)
    i = i + 1
  k = k + 1
  print("".join(encrypt).rstrip())
