#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  a.append(n)
  n = input()

n = input()
b = []
while n != "end":
  b.append(n)
  n = input()

i = 0
j = 0
while i < len(a) or j < len(b):

  if i == len(a):
    print(b[j])
    j = j + 1
  elif j == len(b):
    print(a[i])
    i = i + 1

  elif int(a[i]) < int(b[j]):
    print(a[i])
    i = i + 1
  elif int(b[j]) < int(a[i]):
    print(b[j])
    j = j + 1
  elif int(b[j]) == int(a[i]):
    print(b[j])
    j = j + 1
