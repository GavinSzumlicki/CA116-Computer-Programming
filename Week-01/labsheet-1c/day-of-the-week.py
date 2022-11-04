#!/usr/bin/env python3

month = int(input())
day = int(input())

print(((((month - 1) * 30) + day - 1) % 7) + 1)
