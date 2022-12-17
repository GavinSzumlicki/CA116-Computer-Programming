#!/usr/bin/env python3

#writes the sum of the even Fibonacci numbers which are less than N
import sys
#read the command line argument for desired number
N = int(sys.argv[1])

#variables for fibonacci sequence
prev = 1
curr = 1
sum = 0

#loop that iterates while the current number is less than the desired number
while curr < N:
  tmp = curr
  curr = prev + curr
  prev = tmp

#if statement to check if it is even and less than desired number
  if curr % 2 == 0 and curr < N:
    sum = sum + curr

print(sum)
