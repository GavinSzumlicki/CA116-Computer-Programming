#!/usr/bin/env python3

a = int(input())

b = (a % 10000)
c = (b // 1000)

d = (a % 1000)
e = (d // 100)

print((e * 10) + c)
