#!/usr/bin/env python3

import sys
data = sys.stdin.readlines()

users = []

i = 0
while i < len(data):
  if "".join(data[i]).split("/")[0] not in users:
    users.append("".join(data[i]).split("/")[0])
  i = i + 1

i = 0
while i < len(users):
  p = i
  j = p + 1
  while j < len(users):
    if users[j] < users[p]:
      p = j
    j = j + 1
  tmp = users[i]
  users[i] = users[p]
  users[p] = tmp
  i = i + 1

i = 0
while i < len(users):
  curr = "user-" + str(i + 1)
  count = 0
  corr = []

  j = 0
  while j < len(data):
    task = data[j].split("/")[1].split(".")[0]
    value = data[j].split("/")[1].split(".")[2]
    use = data[j].split("/")[0]

    if use == curr and value == "correct\n":
      count = count + 1
      corr.append(data[j].split("/")[1].split(".")[0])
    elif use == curr and value == "incorrect\n" and task in corr:
      corr.remove(data[j].split("/")[1].split(".")[0])
      count = count - 1
    j = j + 1
  print(curr, count)
  i = i + 1
