#!/usr/bin/env python3

import sys

file_name = "irish-dobs.txt"

with open(file_name) as f:
  data = f.readlines()

data_set = []

i = 0
while i < len(data):
  data[i] = data[i].split("/")
  day = data[i][0]
  month = data[i][1]
  data[i][0] = month
  data[i][1] = day
  data_set.append("/".join(data[i]))
  i = i + 1

with open("american-dobs.txt", "w") as f:
  f.write("".join(data_set))
