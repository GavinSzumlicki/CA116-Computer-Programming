#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

if bmi < 18.5:
  print("underweight")
elif bmi <= 25:
  print("normal")
elif bmi <= 30:
  print("overweight")
else:
  print("obese")
