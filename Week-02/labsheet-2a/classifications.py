#!/usr/bin/env python3

mark = int(input())

print("first:", 70 <= mark)
print("second:", 50 <= mark and mark < 70)
print("third:", 40 <= mark and mark < 50)
print("fail:", mark < 40)
