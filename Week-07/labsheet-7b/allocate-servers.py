#!/usr/bin/env python3

servers = []

s = input()
while s != "end":
  start = int(s)

  i = 0
  while i < len(servers) and not (servers[i] <= start):
    i = i + 1

  if i < len(servers):
    servers[i] = start + 1000

  else:
    servers.append(start + 1000)

  s = input()

print(len(servers))
