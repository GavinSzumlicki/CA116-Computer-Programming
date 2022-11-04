#!/usr/bin/env python3

n = int(input())
m1 = 0
m2 = 1
i = 0

while i < n - 1:
  if m1 == 0:
    print(m1)
    m2 = m1 + m2
    m1 = m2
    print(m1)
  elif m1 < m2:
    print(m2)
    m2 = m1 + m2
    m1 = m2 - m1
  else:
    print(m1)
    m2 = m1 + m2
    m1 = m2 - m1
  i = i + 1
