#!/usr/bin/env python3

n = int(input())
m1 = 0
m2 = 1
i = 0

while i < n - 1:
  if m1 == 0 and m1 < n and m2 < n:
    print(m1)
    m2 = m1 + m2
    m1 = m2
    print(m1)
  elif m1 < m2 and m1 < n and m2 < n:
    print(m2)
    m2 = m1 + m2
    m1 = m2 - m1
  elif m1 < n and m2 < n:
    print(m1)
    m2 = m1 + m2
    m1 = m2 - m1
  i = i + 1
